import requests
from faker import Faker

fake = Faker()

def generate_random_nft():
    response = requests.get('https://picsum.photos/480/640')
    return response.url


def genearte_random_trxID():
    return fake.bothify(text='????####', letters='ABCDE')

def genearte_random_price():
    return fake.random_number(digits=5)


# msg = genearte_random_price()
# print(msg)