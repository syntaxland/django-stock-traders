# settings.py

# Import the MongoClient from the pymongo library
from pymongo import MongoClient

# Connect to MongoDB using the MongoClient
client = MongoClient('mongodb://localhost:27017/')

# Get the database instance
db = client['trader_db']
