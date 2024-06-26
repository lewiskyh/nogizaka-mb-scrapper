from json import JSONDecodeError
import certifi
import os
from dotenv import load_dotenv
import requests
import json
from pymongo import MongoClient

# Load environment variables - MongoDB URI and DB Name etc
load_dotenv()
DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

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

def save_to_mongodb (data):
    # When a client (pymongo) connects to a server (MongoDB Atlas instance)  over TLS the server presents its
    # SSL certificate issued by a CA. The client verifies this certificate against its list of trusted CAs.
    # If the server’s certificate can be traced back to a trusted CA, the connection proceeds securely.

    # tlsCAFILE - specify the path to a CA bundle
    client = MongoClient(DB_URI, tlsCAFile=certifi.where())
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    try:
        # Insert data into MongoDB
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)
        print("Data successfully saved to MongoDB!")
    except Exception as e:
        print(f"An error occurred while saving data to MongoDB: {e}")


def main():
    URL = "https://www.nogizaka46.com/s/n46/api/list/member"
    data = fetch_json(URL)
    if data:
        save_to_mongodb(data)

if __name__ == "__main__":
    main()

