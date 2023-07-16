from flask import Flask, request
from flask_restful import Api, Resource
from src.producer import KafkaProducer

app = Flask(__name__)
api = Api(app)

producer = KafkaProducer()

class MessageResource(Resource):
    def post(self):
        message = request.get_json()
        if not message:
            return {"error": "No message provided"}, 400
        producer.produce_message(message)
        return {"status": "success"}, 200

api.add_resource(MessageResource, '/messages')

if __name__ == "__main__":
    app.run(debug=True)
