import os
import signal
import sys
import subprocess
import shutil
import time
import requests
import api4jenkins
from urllib.parse import quote

slave_jar = '/var/lib/jenkins/slave.jar'
slave_jar_url = os.environ['JENKINS_URL'] + '/jnlpJars/slave.jar'
process = None

def clean_dir(directory):
    for root, dirs, files in os.walk(directory):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

def get_jenkins_instance():
    return api4jenkins.Jenkins(
        os.environ['JENKINS_URL'],
        auth=(os.environ['JENKINS_USER'], os.environ['JENKINS_PASS'])
    )

def sanitize(value):
    """Remove unsafe characters from a string."""
    import re
    return re.sub(r"[^a-zA-Z0-9_-]", "", value)

def slave_exists(jenkins, node_name):
    try:
        node = jenkins.nodes.get(node_name)
        if node:
            print(f"DEBUG: Node '{node_name}' exists.")
            return True
        else:
            print(f"DEBUG: Node '{node_name}' does not exist or cannot be retrieved.")
            return False
    except KeyError:
        print(f"DEBUG: Node '{node_name}' does not exist.")
        return False

def slave_create(node_name, working_dir, executors, labels):
    jenkins = get_jenkins_instance()

    # Sanitize inputs
    node_name = sanitize(node_name)
    labels = sanitize(labels)

    print(f"Creating node '{node_name}' with {executors} executors and labels [{labels}]...")

    try:
        if slave_exists(jenkins, node_name):
            print(f"Node '{node_name}' already exists. Skipping creation as it is likely managed by CasC.")
            return

        # Define node configuration
        node_config = {
            "nodeDescription": "Automatically created by script",
            "numExecutors": int(executors),
            "remoteFS": working_dir,
            "labelString": labels,
            "mode": "NORMAL",  # NORMAL or EXCLUSIVE
            "launcher": {"stapler-class": "hudson.slaves.JNLPLauncher"},
            "retentionStrategy": {"stapler-class": "hudson.slaves.RetentionStrategy$Always"},
        }
        # Add node_config to kwargs
        kwargs = {
            "name": node_name,
            "nodeDescription": node_config["nodeDescription"],
            "numExecutors": node_config["numExecutors"],
            "remoteFS": node_config["remoteFS"],
            "labelString": node_config["labelString"],
            "mode": node_config["mode"],
            "launcher": node_config["launcher"],
            "retentionStrategy": node_config["retentionStrategy"],
        }

        # Create the node
        jenkins.nodes.create(**kwargs)
        print(f"Node '{node_name}' created successfully.")

    except Exception as e:
        print(f"ERROR: Failed to create node '{node_name}': {e}")
        raise


def slave_delete(node_name):
    jenkins = get_jenkins_instance()

    if slave_exists(jenkins, node_name):
        # We don't delete if it might be managed by CasC
        print(f"Node '{node_name}' exists. Skipping deletion to avoid conflict with CasC.")
    else:
        print(f"Node '{node_name}' does not exist. Skipping deletion.")

def slave_download():
    if os.path.isfile(slave_jar):
        os.remove(slave_jar)

    response = requests.get(slave_jar_url, stream=True, verify=False)
    with open(slave_jar, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print("Downloaded Jenkins slave jar.")

def get_slave_secret(slave_name):
    try:
        url = f"{os.environ['JENKINS_URL']}/computer/{slave_name}/jenkins-agent.jnlp"
        auth = (os.environ['JENKINS_USER'], os.environ['JENKINS_PASS'])
        response = requests.get(url, auth=auth, verify=False)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if '<argument>' in line:
                    secret = line.split('<argument>')[1].split('</argument>')[0]
                    return secret
        else:
            raise Exception(f"Failed to fetch slave secret: {response.status_code} {response.reason}")
    except Exception as e:
        print(f"ERROR: Unable to retrieve the slave secret: {e}")
        sys.exit(1)

def slave_run(slave_jar, slave_name):
    jenkins = get_jenkins_instance()

    slave_secret = get_slave_secret(slave_name)
    params = [
        'java', '-jar', slave_jar, '-url', os.environ['JENKINS_URL'], '-name', slave_name, '-secret', slave_secret, '-webSocket'
    ]

    if os.environ.get('JENKINS_SLAVE_ADDRESS'):
        params.extend(['-tunnel', os.environ['JENKINS_SLAVE_ADDRESS']])

    params.append('-workDir')
    params.append(os.getcwd())

    return subprocess.Popen(params, stdout=subprocess.PIPE)

def signal_handler(sig, frame):
    global process
    if process is not None:
        process.send_signal(signal.SIGINT)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def master_ready(url):
    try:
        response = requests.head(url, verify=False, timeout=5)
        return response.status_code == requests.codes.ok
    except requests.RequestException:
        return False

while not master_ready(slave_jar_url):
    print("Master not ready yet, sleeping for 10 seconds!")
    time.sleep(10)

slave_download()

if os.environ.get('SLAVE_WORKING_DIR'):
    os.chdir(os.environ['SLAVE_WORKING_DIR'])

if os.environ.get('CLEAN_WORKING_DIR') == 'true':
    clean_dir(os.getcwd())
    print("Cleaned up working directory.")

slave_name = os.environ.get('SLAVE_NAME', f"docker-slave-{os.environ.get('HOSTNAME')}")
slave_create(slave_name, os.getcwd(), os.environ['SLAVE_EXECUTORS'], os.environ['SLAVE_LABELS'])

process = slave_run(slave_jar, slave_name)
print(f"Started Jenkins slave with name '{slave_name}' and labels [{os.environ['SLAVE_LABELS']}].")
process.wait()

print("Jenkins slave stopped.")
if os.environ.get('SLAVE_NAME') == '':
    slave_delete(slave_name)
    print("Removed temporary Jenkins slave.")