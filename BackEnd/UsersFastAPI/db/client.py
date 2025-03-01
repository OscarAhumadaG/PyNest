from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://test:test@cluster0.qfzqr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
db_client = MongoClient(uri, server_api=ServerApi('1')).test
# Send a ping to confirm a successful connection
try:
    db_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""
uri = "mongodb://localhost:27017/"
db_client = MongoClient(uri).local
"""

