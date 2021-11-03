import json
import requests
import secrets
from os import environ
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID, CLIENT_SECRET = environ['CLIENT_ID'], environ['CLIENT_SECRET']
TOKEN_PATH = "data/mal_token.json"

def mal_read_token():
    try:
        return json.load(open(TOKEN_PATH))
    except:
        raise Exception('Run scripts/mal_generate_token.py first!')


# 1. Generate a new Code Verifier / Code Challenge.
def _get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


# 2. Print the URL needed to authorise your application.
def _print_new_authorisation_url(code_challenge: str):
    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}'
    print(f'Authorise your application by clicking here: {url}\n')


# 3. Once you've authorised your application, you will be redirected to the webpage you've
#    specified in the API panel. The URL will contain a parameter named "code" (the Authorisation
#    Code). You need to feed that code to the application.
def _generate_new_token(authorisation_code: str, code_verifier: str) -> dict:
    if not CLIENT_ID:
        raise Exception('Checkout .env.example')
        
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorisation_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data)
    response.raise_for_status()  # Check whether the requests contains errors

    token = response.json()
    response.close()
    print('Token generated successfully!')

    with open(TOKEN_PATH, 'w', encoding='utf-8') as file:
        json.dump(token, file, indent=4)
        print(f'Token saved in "{TOKEN_PATH}"')

    return token


# 4. Test the API by requesting your profile information
def _print_user_info(access_token: str):
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'
    })

    response.raise_for_status()
    user = response.json()
    response.close()

    print(f"\n>>> Greetings {user['name']}! <<<")


def mal_generate_new_token():
    code_verifier = code_challenge = _get_new_code_verifier()
    _print_new_authorisation_url(code_challenge)

    authorisation_code = input(
        'Copy-paste the Redirected URL or Authorisation Code: ').strip().split('code=')[-1]
    token = _generate_new_token(authorisation_code, code_verifier)

    _print_user_info(token['access_token'])


def mal_refresh_token() -> dict:
    url = 'https://myanimelist.net/v1/oauth2/token'
    old_token = json.load(open(TOKEN_PATH))
    data = {
        'client_id': environ['CLIENT_ID'],
        'client_secret': environ['CLIENT_SECRET'],
        'grant_type': 'refresh_token',
        'refresh_token': old_token['refresh_token']
    }

    response = requests.post(url, data)
    response.raise_for_status()  # Check whether the requests contains errors

    token = response.json()
    response.close()
    print('Refresh Token successfully!')

    with open(TOKEN_PATH, 'w') as file:
        json.dump(token, file, indent=4)
        print(f'Refreshed Token saved in "{TOKEN_PATH}"')

    return token


if __name__ == '__main__':
    mal_generate_new_token()
