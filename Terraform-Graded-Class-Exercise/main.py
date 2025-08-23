import re
import sys
import jinja2
from terraform_template import render_template
from terraform_executor import execute_terraform



def Get_User_Variables():
    # --- AMI selection ---
    ami_choice = input("Choose between Ubuntu or Amazon Linux: ").strip().lower()
    if ami_choice == "ubuntu":
        ami_choice = "ubuntu"
    elif ami_choice in ["amazon linux", "linux"]:
        ami_choice = "amazon linux"
    else:
        sys.exit("❌ You must choose either 'Ubuntu' or 'Amazon Linux'!")
        

    # --- Instance type selection ---
    instance_type_choice = input("Choose instance type (t3.small / t3.medium): ").strip()
    if instance_type_choice == "t3.small":
        instance_type_choice = "t3.small"
    elif instance_type_choice == "t3.medium":
        instance_type_choice = "t3.medium"
    else:
        sys.exit("❌ You must choose either 't3.small' or 't3.medium'!")


    # --- Region selection ---
    region = input("Select region (only 'us-east-2' is allowed, others will be defaulted): ").strip()
    if region != "us-east-2":
        print(f"⚠️ Region '{region}' is not allowed. Defaulting to 'us-east-2'.")
        region = "us-east-2"

    # --- Load Balancer name ---
    alb_name = input("Enter a name for your Load Balancer (ALB): ").strip()

    if not re.match(r'^[a-zA-Z0-9\-]+$', alb_name):
        sys.exit("❌ Invalid ALB name. Use only letters, numbers, and hyphens (-).")

    print("\n✅ Summary of your configuration:")
    print(f"  AMI:            {ami_choice}")
    print(f"  Instance Type:  {instance_type_choice}")
    print(f"  Region:         {region}")
    print(f"  ALB Name:       {alb_name}")

    # --- Store all values in a dictionary ---
    context = {
        "ami": ami_choice,
        "instance_type": instance_type_choice,
        "region": region,
        "availability_zone": "us-east-2",
        "lb_name": alb_name
    }

    print("\n✅ Configuration collected successfully!")
    print("Context to pass into Jinja2 template:")
    print(context)

    # --- Jinja2 template usage ---
    template_str = """
          resource "aws_instance" "example" {
            ami         = "{{ ami }}"
            instance_type = "{{ instance_type }}"
            region        = "{{ region }}"
          }

          resource "aws_lb" "example" {
            name = "{{ lb_name }}"
            internal           = false
            load_balancer_type = "application"
            subnets            = ["subnet-xyz"]  # Replace with real subnet IDs
          }
          """

    # Render the template
    try:
        template = jinja2.Template(template_str)
        rendered_output = template.render(context)

        print("\n📄 Rendered Terraform Configuration:")
        print(rendered_output)
        return context

    except jinja2.exceptions.TemplateError as e:
        print("\n❌ Jinja2 template rendering failed!")
        print(f"Error: {e}")




if __name__ == '__main__':
    print("Build a Python-based AWS Infrastructure as Code (IaC) tool!")
    print("Please enter the following details to create your infrastructure.\n")

    context = Get_User_Variables()

    rendered_tf = render_template(context)


    execute_terraform(rendered_tf, "./terraform/main.tf")
    validate_resources("./terraform")


