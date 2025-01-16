import os
from jinja2 import Template

# Define the variables for the template
variables = {
    "credentials_id": "my-credentials-id",
    "k8s_endpoint_url": "https://kubernetes.example.com",
    "database_endpoint": "mysql://db.example.com:3306"
}

# Load the Jinja2 template
# Change to the script directory or python wont find the file
FOLDER = os.path.dirname(__file__)
# Contcat the folder and the file name
TEMPLATE = os.path.join(FOLDER, "pipeline_template.j2")
with open(FOLDER, "r") as file:
    template_content = file.read()

# Render the template
template = Template(template_content)
jenkinsfile_content = template.render(variables)

# Save the rendered pipeline to a Jenkinsfile
with open("Jenkinsfile", "w") as file:
    file.write(jenkinsfile_content)

print("Jenkinsfile generated successfully.")