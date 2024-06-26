from json import JSONDecodeError

import pymongo
import requests
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Extract json from the response
        json_str = response.text.strip()[4:-2] # Remove "res (" and " ); "
        data = json.loads(json_str)
        return data

    except requests.exceptions.RequestException as e:
        print(f"(Request error: {e} )")
    except JSONDecodeError as e:
        print(f"(json decoding error: {e} )")


def save_to_mongodb ():
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    uri = "mongodb+srv://lewiskwokyh:29YrIcfBnvKPo3yI@cluster0.xpzvbiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def main():
    ##URL = "https://www.nogizaka46.com/s/n46/api/list/member"
    ##data = fetch_json(URL)

    save_to_mongodb()

