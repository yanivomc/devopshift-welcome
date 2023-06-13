from flask import Flask, render_template, request, jsonify
import pika # for RabbitMQ
from pymongo import MongoClient # to connect to MongoDB
import os

app = Flask(__name__)

# Debug flag
app.config['DEBUG'] = os.environ.get('DEBUG', 'True').lower() == 'true'

# Mock data
mock_nfts = [
    {"nftid": "1", "nftimage_url": "https://placekitten.com/200/300", "nftdescription": "Description of NFT 1", "price": "100"},
    {"nftid": "2", "nftimage_url": "https://placekitten.com/200/301", "nftdescription": "Description of NFT 2", "price": "200"},
    {"nftid": "3", "nftimage_url": "https://placekitten.com/200/302", "nftdescription": "Description of NFT 3", "price": "300"},
    {"nftid": "4", "nftimage_url": "https://placekitten.com/200/303", "nftdescription": "Description of NFT 4", "price": "400"},
    {"nftid": "5", "nftimage_url": "https://placekitten.com/200/304", "nftdescription": "Description of NFT 5", "price": "500"},
    {"nftid": "6", "nftimage_url": "https://placekitten.com/200/305", "nftdescription": "Description of NFT 6", "price": "600"},
    {"nftid": "7", "nftimage_url": "https://placekitten.com/200/306", "nftdescription": "Description of NFT 7", "price": "700"},
    {"nftid": "8", "nftimage_url": "https://placekitten.com/200/307", "nftdescription": "Description of NFT 8", "price": "800"},
    {"nftid": "9", "nftimage_url": "https://placekitten.com/200/308", "nftdescription": "Description of NFT 9", "price": "900"},
    {"nftid": "10", "nftimage_url": "https://placekitten.com/200/309", "nftdescription": "Description of NFT 10", "price": "1000"},
]

# In-memory data
sold_nfts_list = []

if not app.config['DEBUG']:
    import pika # for RabbitMQ
    from pymongo import MongoClient # to connect to MongoDB

    # setup RabbitMQ connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # replace 'localhost' with your RMQ server
    channel = connection.channel()

    # setup MongoDB connection
    client = MongoClient('mongodb://localhost:27017/') # replace with your MongoDB connection string
    db = client['nft_db'] # replace 'nft_db' with your MongoDB database name
    nft_collection = db['nft_collection'] # replace 'nft_collection' with your MongoDB collection name

@app.route('/')
def home():
    if app.config['DEBUG']:
        nfts = mock_nfts
    else:
        nfts = list(nft_collection.find({}))
    return render_template('home.html', nfts=nfts)

@app.route('/buy', methods=['POST'])
def buy():
    clientname = request.form.get('clientname')
    nftid = request.form.get('nftid')
    nftprice = request.form.get('nftprice')
    nftimage_url = request.form.get('nftimage_url')

    if app.config['DEBUG']:
        sold_nfts_list.append({
            'clientname': clientname,
            'nftid': nftid,
            'nftprice': nftprice,
            'nftimage_url': nftimage_url
        })
        
        message={
            'msg': 'Sold nfts list',
            'soldlist': sold_nfts_list,
            'request': request
        }
        print(message)
    else:
        # send data to RabbitMQ!
        channel.basic_publish(exchange='', routing_key='products', body=f'{clientname},{nftid},{nftprice},{nftimage_url}')

    return jsonify({'status': 'success'})

@app.route('/nft-sold', methods=['GET', 'POST'])
def sold_nfts():
    if request.method == 'POST':
        if app.config['DEBUG']:
            sold = sold_nfts_list
        else:
            sold = list(nft_collection.find({}))
        return jsonify(sold)  # return data as JSON for POST requests

    else:  # GET request
        if app.config['DEBUG']:
            message={
                'msg': 'Sold nfts list',
                'soldlist': sold_nfts_list
            }
            print(message)
            sold = sold_nfts_list
        else:
            sold = list(nft_collection.find({}))
        return render_template('sold_nfts.html', data=sold)  # render HTML for GET requests

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)