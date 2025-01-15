import subprocess

# Run a command and stream its output
with subprocess.Popen(["ping", "-c", "4", "8.8.8.8"], stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line.strip())
