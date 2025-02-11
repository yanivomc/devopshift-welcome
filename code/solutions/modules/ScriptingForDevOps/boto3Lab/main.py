import boto3
import botocore.exceptions

def list_s3_buckets():
    """Lists all S3 buckets."""
    s3 = boto3.client("s3")
    try:
        response = s3.list_buckets()
        print("S3 Buckets:")
        for bucket in response["Buckets"]:
            print(f"- {bucket['Name']}")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def create_s3_bucket():
    """Creates an S3 bucket."""
    s3 = boto3.client("s3")
    bucket_name = input("Enter the name for the new bucket: ")
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def delete_s3_bucket():
    """Deletes an S3 bucket."""
    s3 = boto3.client("s3")
    bucket_name = input("Enter the name of the bucket to delete: ")
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully!")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def list_ec2_instances():
    """Lists all running EC2 instances."""
    ec2 = boto3.client("ec2")
    try:
        response = ec2.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def start_ec2_instance():
    """Starts an EC2 instance."""
    ec2 = boto3.client("ec2")
    instance_id = input("Enter the Instance ID to start: ")
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting EC2 instance {instance_id}")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def stop_ec2_instance():
    """Stops an EC2 instance."""
    ec2 = boto3.client("ec2")
    instance_id = input("Enter the Instance ID to stop: ")
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping EC2 instance {instance_id}")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

def main():
    while True:
        print("\nAWS Resource Manager")
        print("1. Manage S3 Buckets")
        print("2. Manage EC2 Instances")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("\nS3 Management:")
            print("1. List Buckets")
            print("2. Create Bucket")
            print("3. Delete Bucket")
            s3_choice = input("Choose an action: ")
            if s3_choice == "1":
                list_s3_buckets()
            elif s3_choice == "2":
                create_s3_bucket()
            elif s3_choice == "3":
                delete_s3_bucket()
        elif choice == "2":
            print("\nEC2 Management:")
            print("1. List Instances")
            print("2. Start Instance")
            print("3. Stop Instance")
            ec2_choice = input("Choose an action: ")
            if ec2_choice == "1":
                list_ec2_instances()
            elif ec2_choice == "2":
                start_ec2_instance()
            elif ec2_choice == "3":
                stop_ec2_instance()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()