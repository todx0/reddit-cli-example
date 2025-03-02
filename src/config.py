from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('PASSWORD')
        self.user_agent = os.environ.get('USER_AGENT')
        self.validate()

    def validate(self):
        required = ['client_id', 'client_secret', 'username', 'password', 'user_agent']
        missing = [var for var in required if getattr(self, var) is None]
        if missing:
            raise ValueError(f"Missing environment variables: {', '.join(missing)}")