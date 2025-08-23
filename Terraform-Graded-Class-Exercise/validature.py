

import boto3
import json

def validate_with_boto3(instance_id: str, alb_dns: str, region: str = "us-east-2"):
    try:
        ec2 = boto3.client("ec2", region_name=region)
        elbv2 = boto3.client("elbv2", region_name=region)

        # get instance details
        ec2_response = ec2.describe_instances(InstanceIds=[instance_id])
        reservations = ec2_response.get("Reservations", [])
        if not reservations or not reservations[0]["Instances"]:
            raise Exception("EC2 instance not found.")

        instance = reservations[0]["Instances"][0]
        instance_state = instance["State"]["Name"]
        public_ip = instance.get("PublicIpAddress", "N/A")

        # get ALB details
        lb_response = elbv2.describe_load_balancers()
        lb_dns_name = None
        for lb in lb_response["LoadBalancers"]:
            if alb_dns in lb["DNSName"]:
                lb_dns_name = lb["DNSName"]
                break

        if not lb_dns_name:
            raise Exception("ALB not found.")

        # Store to JSON
        validation_data = {
            "instance_id": instance_id,
            "instance_state": instance_state,
            "public_ip": public_ip,
            "load_balancer_dns": lb_dns_name
        }

        with open("aws_validation.json", "w") as f:
            json.dump(validation_data, f, indent=4)

        print("AWS resource validation complete. Output written to aws_validation.json")

    except Exception as e:
        print(f"Boto3 validation failed: {str(e)}")


validate_with_boto3(
    instance_id="i-014c78c8124d22438",
    alb_dns="tomer-lb-1577578029.us-east-2.elb.amazonaws.com"
)

