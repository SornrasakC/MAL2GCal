'''
This script will attempt to open your webbrowser,
perform OAuth 2.0 authentication and print your access token.
To install dependencies from PyPI:
  $ pip install oauth2client
Then run this script:
  $ python get_oauth2_token.py
This is a combination of snippets from:
  https://developers.google.com/api-client-library/python/guide/aaa_oauth
  https://gist.github.com/burnash/6771295
'''

from oauth2client.client import OAuth2WebServerFlow, OAuth2Credentials  # type: ignore
from oauth2client.tools import run_flow  # type: ignore
from oauth2client.file import Storage  # type: ignore

import httplib2 # type: ignore
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI # type: ignore

import json
import os
import sys
from os import environ
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID, CLIENT_SECRET = environ['G_CLIENT_ID'], environ['G_CLIENT_SECRET']
TOKEN_PATH = "data/g_token.json"


def g_read_token():
    try:
        return json.load(open(TOKEN_PATH))
    except:
        raise Exception('Run scripts/optionals/g_generate_token.py first!')


def disable_stout():
    o_stdout = sys.stdout
    o_file = open(os.devnull, 'w')
    sys.stdout = o_file
    return (o_stdout, o_file)


def enable_stout(o_stdout, o_file):
    o_file.close()
    sys.stdout = o_stdout


def g_generate_new_token():
    if not CLIENT_ID:
        raise Exception('Checkout .env.example')

    SCOPE = 'https://www.googleapis.com/auth/calendar'
    REDIRECT_URI = 'http://localhost/oauth'

    o_stdout, o_file = disable_stout()

    flow = OAuth2WebServerFlow(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope=SCOPE,
        redirect_uri=REDIRECT_URI)

    storage = Storage('data/g_token.json')
    credentials = run_flow(flow, storage)
    enable_stout(o_stdout, o_file)

    print(f"access_token: {credentials.access_token}")

    return credentials.access_token


def g_refresh_token():

    CLIENT_ID, CLIENT_SECRET = environ['G_CLIENT_ID'], environ['G_CLIENT_SECRET']
    REFRESH_TOKEN = g_read_token()['refresh_token']

    credentials = OAuth2Credentials(
        access_token=None,  # set access_token to None since we use a refresh token
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        refresh_token=REFRESH_TOKEN,
        token_expiry=None,
        token_uri=GOOGLE_TOKEN_URI,
        user_agent=None,
        revoke_uri=GOOGLE_REVOKE_URI)

    credentials.refresh(httplib2.Http())  # refresh the access token (not optional)
    new_token = json.loads(credentials.to_json())

    with open(TOKEN_PATH, 'w') as file:
        json.dump(new_token, file, indent=4)
        print(f'Refreshed Token saved in "{TOKEN_PATH}"')


if __name__ == '__main__':
    g_generate_new_token()
