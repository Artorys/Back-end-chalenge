import os 
from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("POSTGRES_URL")
ALLOWED_EXTENSIONS = ["txt"]
UPLOAD_FOLDER = os.getcwd() + "/app/upload/"