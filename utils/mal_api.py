import requests
from utils import mal_read_token
from collections import namedtuple

headers = {'Authorization': f'Bearer {mal_read_token()["access_token"]}'}
# headers = {'X-MAL-CLIENT-ID': MAL_CLIENT_ID} // TODO change method to this https://myanimelist.net/forum/?topicid=1973077

BASE_URL = 'https://api.myanimelist.net/v2'


def _parse(params):
    return '&'.join(f'{k}={v}' for k, v in params.items())

STATUS = namedtuple('Status', "W P")(W='watching', P='plan_to_watch')

def _mal_api_all_status_ids(status):
    params = {
        'fields': '',
        'limit': '1000',
        'status': status
    }

    url = f'{BASE_URL}/users/@me/animelist?{_parse(params)}'
    res = requests.get(url, headers=headers)
    data = res.json()['data']

    return [d['node']['id'] for d in data]

def mal_api_all_watching_ids():
    return _mal_api_all_status_ids(STATUS.W)


def mal_api_all_plan_ids():
    return _mal_api_all_status_ids(STATUS.P)


def mal_api_anime_detail(id):
    params = {
        'fields': 'title,start_date,end_date,num_episodes'
    }

    url = f'{BASE_URL}/anime/{id}?{_parse(params)}'
    res = requests.get(url, headers=headers)
    data = res.json()

    return data


def mal_api_batch_anime_detail(ids):
    return [mal_api_anime_detail(id) for id in ids]
