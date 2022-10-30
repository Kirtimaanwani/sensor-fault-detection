# write code that shown in class here for mongodb_connection
import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.credentials.CREDENTIALS import MONGO_DB_URL
import certifi
ca = certifi.where()

from credential.CREDENTIAL import MONGO_DB_URL

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                MongoDBClient.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e