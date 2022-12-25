import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# Connect to MongoDB
mongo_user = os.getenv("user")
mongo_pass = os.getenv("password")
mongo_cluster = os.getenv("cluster_address")

client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_cluster}")

metrics = client.metrics
ohlcv_db = metrics.ohlcv_db
posts_db = metrics.posts_db

print(ohlcv_db.count_documents({}))