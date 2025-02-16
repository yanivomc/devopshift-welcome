import boto3
import random

# s3_client = boto3.client("s3")
# response = s3_client.list_buckets()

# for bucket in response["Buckets"]:
#     print(f"Buckets: {bucket['Name']}")
def main():
    while True:
        user_choice = input("[1] Manage S3 Buckets\n[2] Manage EC2 Instances\n[3] Exit\n")
        if user_choice == "1":
            s3_client = boto3.client("s3")
            user_choice = input("chose an option: list, create, delete: ")
            if user_choice == "list":
                list_bucket(s3_client)
            elif user_choice == "create":
                create_bucket(s3_client)
            elif user_choice == "delete":
                delete_bucket()
            else:
                print("Please chose a valid option from the menu")
        elif user_choice =="2":
            ec2_client = boto3.client("ec2")
            user_choice = input("chose an option: list, start, stop, terminate: ")
            if user_choice == "list":
                list_instances(ec2_client)
            elif user_choice == "start":
                pass
            elif user_choice == "stop":
                pass
            elif user_choice == "terminate":
                pass
            else:
                print("Please chose a valid option from the menu")
        elif user_choice == "3":
            break
        else:
            print("Please chose a valid option from the menu")
            
            
            
def list_bucket(s3_client):
    response = s3_client.list_buckets()
    try:
        for bucket in response["Buckets"]:
            print(f"Buckets: {bucket['Name']}")
    except KeyError:
        print("no bucket was found")
def create_bucket(s3_client):
    bucket_name = input("Please enter the new bucket name: ")
    response = s3_client.create_bucket(
        Bucket=bucket_name
        )
    print(bucket_name + " was created")     
def delete_bucket(s3_client):
        bucket_name = input("Please type the name of the bucket you want to delete: ")
        response = s3_client.delete_bucket(
            Bucket=bucket_name,
            ExpectedBucketOwner='???'
                
        )
def list_instances(ec2_client):
    response = ec2_client.describe_instances()
    try:
        for instance in response["Instances"]:
            print(f"Instance: {instance['Name']}")
    except KeyError:
        print("no instance was found")
    

if __name__ == '__main__': 
    main() 
        