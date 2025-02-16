import boto3
import os

def list_bucket(s3_client):
    response = s3_client.list_buckets()
    try:
        for bucket in response["Buckets"]:
            print(f"Buckets: {bucket['Name']}")
    except KeyError:
        print("No buckets were found")
def create_bucket(s3_client):
    bucket_name = input("Please chose a name for the new bucket: ")
    response = s3_client.create_bucket(
        Bucket=bucket_name
        )
    print(bucket_name + " was created")     
def delete_bucket(s3_client):
        bucket_name = input("Please type the name of the bucket you want to delete: ")
        bucket_owner = input("Please type the name of the owner: ")
        response = s3_client.delete_bucket(
            Bucket=bucket_name,
            ExpectedBucketOwner=bucket_owner               
        )
def s3_menu():
        s3_client = boto3.client("s3")
        while True:
            print("Welcome to S3 menu. Please choose what you want to do:")
            user_choice = input("[1] List of all buckets.\n[2] Create a new bucket.\n[3] Delete bucket.\n[4] Go back to main menu.\n")
            match user_choice:
                case "1":
                    list_bucket(s3_client)
                case "2":
                    create_bucket(s3_client)
                case "3":
                    delete_bucket(s3_client)
                case "4":
                    print("Exited to main menu.")
                    return
                case default:
                    print("Invalid option. Please select again.")
                

def ec2_menu():
    pass

def menu():
    os.environ['AWS_ACCESS_KEY_ID'] = input("AWS_ACCESS_KEY_ID: ").strip()
    os.environ['AWS_SECRET_ACCESS_KEY'] = input("AWS_SECRET_ACCESS_KEY: ").strip()
    os.environ['AWS_DEFAULT_REGION'] = input("AWS_DEFAULT_REGION: ").strip()
    while True:
        user_choice = input("Chose an option from the menu:\n[1] Manage S3 Buckets\n[2] Manage EC2 Instances\n[3] Exit\n")
        match user_choice:
            case "1":
                s3_menu()
            case "2":
                ec2_menu()
            case "3":
                break
            case default:
                print("Invalid option. Please select again.")
                
        


def main():
    menu()
if __name__ == "__main__":
    main()