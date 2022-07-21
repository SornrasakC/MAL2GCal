
from utils import g_read_token
import httplib2 # type: ignore
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client # type: ignore

from os import environ
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID, CLIENT_SECRET = environ['G_CLIENT_ID'], environ['G_CLIENT_SECRET']
REFRESH_TOKEN = g_read_token()['refresh_token']

credentials = client.OAuth2Credentials(
    access_token=None,  # set access_token to None since we use a refresh token
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    refresh_token=REFRESH_TOKEN,
    token_expiry=None,
    token_uri=GOOGLE_TOKEN_URI,
    user_agent=None,
    revoke_uri=GOOGLE_REVOKE_URI)

credentials.refresh(httplib2.Http())  # refresh the access token (optional)
print(credentials.to_json())
# http = credentials.authorize(httplib2.Http())