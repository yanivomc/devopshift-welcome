Step 1: Launch EC2 Instances with UserData

Go to the AWS Management Console and navigate to the EC2 service.
Click on "Launch Instance" to start the instance creation wizard.
Choose an Amazon Machine Image (AMI) that suits your requirements. For this example, select an Amazon Linux 2 AMI.
Select an instance type (e.g., t2.micro).
In the "Configure Instance Details" section:
Choose the desired VPC and Subnets.
Enable "Auto-assign Public IP" to allow the instances to have public IP addresses.
In the "Advanced Details" section, enter the following UserData script:
bash
Copy code
#!/bin/bash
yum update -y
yum install nginx -y
echo "<html><body><h1>Instance Name: $(curl http://169.254.169.254/latest/meta-data/hostname)</h1></body></html>" > /usr/share/nginx/html/index.html
service nginx start
This script updates the instance, installs Nginx, and creates a custom HTML page showing the instance name when browsing it.

Proceed with the instance launch and create two instances in different Availability Zones (AZs).
Step 2: Create an Auto Scaling Group (ASG)

Go to the AWS Management Console and navigate to the EC2 service.
In the left sidebar, click on "Auto Scaling Groups."
Click on "Create Auto Scaling Group."
Choose the instances created in Step 1 for the ASG:
Select the same VPC and Subnets where the instances were created.
In "Advanced Details," set the desired number of instances (e.g., 2) in the ASG.
Configure the scaling policies as per your requirements (e.g., scaling up or down based on CPU utilization).
In "Add Tags," add any tags you need for identification purposes.
Review the configuration, and click "Create Auto Scaling Group."
Step 3: Create a Load Balancer

Follow the steps mentioned in the previous response to create an Elastic Load Balancer (ELB).

Step 4: Associate Instances with the Load Balancer

Once the Auto Scaling Group is created, go to the AWS Management Console and navigate to the EC2 service.
Under "Instances," select the two instances created in Step 1.
Click on "Instance Settings" in the top menu, and then click on "Attach to Auto Scaling Group."
Choose the Auto Scaling Group created in Step 2 and click "Attach."
Now, you have a fully functional EC2 deployment with a Load Balancer and Auto Scaling Group. The instances will automatically register with the load balancer, and the ASG will ensure that the desired number of instances (2) is always running. The load balancer will distribute traffic across the instances in the ASG. You can access your custom HTML page using the External DNS of the load balancer.