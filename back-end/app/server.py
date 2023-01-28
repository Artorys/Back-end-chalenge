from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

PORT = os.getenv("DB_PORT")

def connect_db():
    try:
        db = MongoClient(host=[f"localhost:{PORT}"])
        db = db.test
        return db
    except pymongo.errors.AutoReconnect:
        print("Tentando conexao com o MONGODB")
    
    