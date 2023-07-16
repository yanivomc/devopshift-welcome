from flask import Flask, render_template, request, jsonify, redirect, url_for
import pika # for RabbitMQ 
import json
from pymongo import MongoClient # to connect to MongoDB
import os
import src.generators.nftGenerator as nftGenerator
import requests
app = Flask(__name__)

# Debug flag
app.config['DEBUG'] = os.environ.get('DEBUG', 'True').lower() == 'true'


DEBUG_RMQ = os.environ.get('DEBUG_RMQ', False)
DEBUG_MONGO = os.environ.get('DEBUG_MONGO', False)

# # RabbitMQ Configuration - refactored out 
# RMQ_HOST = os.getenv("RMQ_HOST", "localhost")
# RMQ_QUEUE = os.getenv("RMQ_QUEUE", "sold-nft")
# RMQ_QUEUE_DLX = os.getenv("RMQ_QUEUE_DLX", "dead-letter-sold-nfts")
# RMQ_QUEUE_MV = os.getenv("RMQ_QUEUE_MV", "sold-nfts-mv")
# RMQ_USERNAME = os.getenv("RMQ_USERNAME", "guest")
# RMQ_PASSWORD = os.getenv("RMQ_PASSWORD", "123456")


# Mongo Configuration
MONGO_HOST = os.getenv("MONGO_HOST", 'mongodb://root:pass12345@localhost:27017/')
# Mock data
x = 0
mock_nfts = []
loadingnft="############### LOADING NFT'S PLEASE WAIT ###################"
print(loadingnft)
while (x < 10):
    nft={
          "nftid": nftGenerator.genearte_random_trxID(), 
          "nftimage_url": nftGenerator.generate_random_nft(),
          "nftdescription": "Description of NFT", 
          "price": nftGenerator.genearte_random_price()
          }
    mock_nfts.append(nft)
    x+=1



# In-memory data
sold_nfts_list = []

if not DEBUG_RMQ == True:
    import pika # for RabbitMQ
    from pymongo import MongoClient # to connect to MongoDB


    # setup RabbitMQ connection - refactor out
    # credentials = pika.PlainCredentials(RMQ_USERNAME, RMQ_PASSWORD)
    # parameters = pika.ConnectionParameters(host=RMQ_HOST, credentials=credentials)
    # rmq_connection = pika.BlockingConnection(parameters)
    # channel = rmq_connection.channel()

    # setup MongoDB connection
    if not DEBUG_MONGO == True:
        client = MongoClient(MONGO_HOST)
        db = client['nft_db'] # replace 'nft_db' with your MongoDB database name
        sold_nfts_mv_collections = db['sold_nfts_mv_collections'] # replace 'nft_collection' with your MongoDB collection name

@app.route('/')
def home():
    # if DEBUG_MONGO == True :
    nfts = mock_nfts
    # else:
        # nfts = list(nft_collection.find({}))
    return render_template('home.html', nfts=nfts)

@app.route('/buy', methods=['POST'])
def buy():
    clientname = request.form.get('clientname')
    nftid = request.form.get('nftid')
    nftprice = request.form.get('nftprice')
    nftimage_url = request.form.get('nftimage_url')
    trx_id = nftGenerator.genearte_random_trxID()

    if DEBUG_RMQ == True:
        sold_nfts_list.append({
            'clientname': clientname,
            'nftid': nftid,
            'nftprice': nftprice,
            'nftimage_url': nftimage_url,
            'trx_id': trx_id
        })
        
        message={
            'msg': 'Sold nfts list',
            'soldlist': sold_nfts_list,
            'request': request
        }
        print(message)
    else:
        # send data to RabbitMQ!
        body_dict = {"trx_status":"pending", "trx_id": trx_id,"clientname": clientname, "nftid": nftid, "nftprice": float(nftprice), "nftimage_url": nftimage_url}
        # body = json.dumps(body_dict)
        try:
            response = requests.post('http://localhost:8082/messages', json=body_dict)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return jsonify({'status': 'error'})
        return jsonify({'status': 'success'})


        #Disabling RMQ - Refactoring into KAFKA Producer sidecar
        # channel.basic_publish(exchange='sold_nft_ex', routing_key='', body=body)
        


    return jsonify({'status': 'success'})

@app.route('/nft-sold', methods=['GET', 'POST'])
def sold_nfts():
    if request.method == 'POST':
        if DEBUG_MONGO == True:
            sold = sold_nfts_list
        else:
            sold = list(sold_nfts_mv_collections.find({}))
        return jsonify(sold)  # return data as JSON for POST requests

    else:  # GET request
        if  DEBUG_MONGO == True:
            message={
                'msg': 'Sold nfts list',
                'soldlist': sold_nfts_list
            }
            print(message)
            sold = sold_nfts_list
        else:
            sold = list(sold_nfts_mv_collections.find({}))
        return render_template('sold_nfts.html', data=sold)  # render HTML for GET requests

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081 ,debug=True)