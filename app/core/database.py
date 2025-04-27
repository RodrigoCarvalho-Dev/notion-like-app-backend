from pymongo import AsyncMongoClient
from pymongo.database import Database
import os



class MongoDB:
    
    client: AsyncMongoClient | None = None
    
    @classmethod
    async def init_db(cls):
        if cls.client is None:
            cls.client = AsyncMongoClient(os.getenv("MONGODB_URL"))
        else: 
            raise Exception("Database already initialized.")
        return cls.client
    
    @classmethod
    async def close_db(cls):
        if cls.client:
            await cls.client.close()
            cls.client = None
            
    @classmethod
    async def get_db(cls) -> Database:
        if cls.client is None:
            raise Exception("Database not initialized. Call init_db() first.")
        
        database : Database = cls.client.get_database(os.getenv("MONGODB_DB_NAME")) 
    
        return database 


