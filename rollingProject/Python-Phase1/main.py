from fastapi import FastAPI, Request
import terraform.management as terraform
import boto3

# Create a FastAPI instance
app = FastAPI()

@app.post("/provision")
async def provision(request: Request):  # Use Request to get query parameters
    action = request.query_params.get("action")  # Access the query parameter
    match action:
        case "destroy":
            # Call Destroy function from terraform.managment module
            return terraform.destroy()
        case "provision":
            # Call Provision function from terraform.managment module
            return terraform.provision()
        case _:
            return {"message": "Invalid action", "status": "error"}

@app.get("/monitor")
def monitor():
    # Mock AWS monitoring response
    return {"instances": [{"id": "i-1234567890", "status": "running"}]}

@app.get("/list-regions")
def list_regions():
  # Create an EC2 client object
  ec2 = boto3.client("ec2")
  #Mocking regions in AWS
  regions = [{"RegionName": "us-east-1"}, {"RegionName": "us-west-1"}, {"RegionName": "us-west-2"}, {"RegionName": "eu-west-1"}]
  return {"regions": [region["RegionName"] for region in regions]} 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

