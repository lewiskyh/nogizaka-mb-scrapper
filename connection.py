from pymongo import MongoClient

CONNECTION_STR = "mongodb+srv://lewiskwokyh:29YrIcfBnvKPo3yI@cluster0.xpzvbiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def test_connection():
    try:
        client = MongoClient(CONNECTION_STR)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_connection()