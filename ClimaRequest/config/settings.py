import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = [
    {
        "name": "OpenWeather",
        "api_class": "OpenWeatherService",
        "city": os.getenv("OW_CITY"),
        "api_key": os.getenv("OW_KEY"),
    }, 
    {
        "name": "ClimaTempo",
        "api_class": "ClimaTempoService",
        "city": os.getenv("CT_CITY"),
        "api_key": os.getenv("CT_KEY"),
    }
]

FIREBASE_URL = os.getenv("FIREBASE_URL")
FIREBASE_CRED = os.getenv("FIREBASE_CRED")