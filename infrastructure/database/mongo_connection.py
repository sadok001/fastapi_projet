from pymongo import MongoClient

from infrastructure.core.config import settings

mongo_client = MongoClient(settings.MONGO_CON_URL)
db = mongo_client.test_fastapi
