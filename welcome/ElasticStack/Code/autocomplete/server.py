from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

ES_HOST = 'http://54.213.6.220:9200'  # Change this to your Elasticsearch instance URL
ES_USER = 'elastic'
ES_PASS = 'changeme'

es = Elasticsearch([ES_HOST], http_auth=(ES_USER, ES_PASS))

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    body = {
        "query": {
            "prefix": {
                "title": keyword
            }
        }
    }
    response = es.search(index="movielens", body=body)
    return jsonify(response['hits']['hits'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5200)
