from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv

load_dotenv()

# Load from environment variables
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    raise ValueError("Missing Google OAuth credentials. Please check .env file")

oauth = OAuth()

def init_oauth(app):
    oauth.init_app(app)

    google = oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        access_token_url='https://oauth2.googleapis.com/token',
        authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
        api_base_url='https://openidconnect.googleapis.com/v1/',
        client_kwargs={'scope': 'openid email profile'},
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
    )
    return google
