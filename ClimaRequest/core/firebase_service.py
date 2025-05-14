import firebase_admin
from firebase_admin import credentials, db
from models.clima import Clima

class FirebaseService:
    def __init__(self, url: str, cred_path: str) -> None: 
        """
        Initializes the Firebase service with the URL and credentials file path.
        :param url: URL of the Firebase Realtime Database.
        :param cred_path: Path to the Firebase credentials JSON file.
        """
        app_name = f"app_{url.split('//')[1]}"
        cred = credentials.Certificate(cred_path)
        self.app = firebase_admin.initialize_app(cred, {
            'databaseURL': url
        }, name=app_name)
        self.ref = db.reference("clima", self.app)
        
    def send(self, clima: Clima) -> None:
        """
        Sends the weather data to Firebase.
        :param clima: Clima object to be sent to Firebase.
        """
        self.ref.push(clima.to_dict())