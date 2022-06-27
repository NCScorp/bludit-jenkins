import os
from dotenv import load_dotenv

load_dotenv('.env')

TOKEN_API = os.environ.get("TOKEN_API")
AUTHENTICATION = os.environ.get("AUTHENTICATION")
BASE_URL = 'http://localhost:8000'
AVULSOS = os.environ.get("AVULSOS")
MASTER = os.environ.get("MASTER")
CDN_NASAJON = os.environ.get("CDN_NASAJON")
CDN_NASAJON_PATH = os.environ.get("CDN_NASAJON_PATH")
STATIC_NASAJON = os.environ.get("STATIC_NASAJON")