import requests
import json



class avroManager:
    def __init__(self,avroSchema, registryUrl='http://localhost:8081', topicName='sold_nft_ex-value'):
# Define the schema registry URL and the subject
        self.schema_registry_url = registryUrl
        self.subject = topicName  # replace with your topic name and whether it's a key or value schema

        # Define the schema
        self.schema = avroSchema


        # Define the payload with the schema
        self.payload = {
            "schema": json.dumps(self.schema)
        }
    def manageRegistry(self):
        # Send the POST request to the Schema Registry
        response = requests.post(f'{self.schema_registry_url}/subjects/{self.subject}/versions', json=self.payload)

        # Print the response
        print(response.json())
