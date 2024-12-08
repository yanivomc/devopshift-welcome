import subprocess

def provision ():
    # Mock Terraform provisioning response
    try:
        subprocess.run(["echo", "running terraform init"])
        subprocess.run(["echo", "running terraform plan"])
    except:
        return {"message": "Infrastructure provisioning failed", "status": "mocked"}
    
    return {"message": "Infrastructure provisioned successfully", "status": "mocked"}


def destroy ():
    # Mock Terraform destroy response
    try:
        subprocess.run(["echo", "running terraform destroy"])
    except:
        return {"message": "Infrastructure destroy failed", "status": "mocked"}

    return {"message": "Infrastructure destroyed successfully", "status": "mocked"}
