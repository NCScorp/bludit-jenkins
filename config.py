import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv('.env')

TOKEN_API = os.environ.get("TOKEN_API")
AUTHENTICATION = os.environ.get("AUTHENTICATION")
BASE_URL = 'http://localhost:8000'
