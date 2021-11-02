import json

from utils.token_utils import generate_new_token, refresh_token, read_token
from utils.mal_api import api_all_watching_ids, api_anime_detail, api_batch_anime_detail

def create_anime_lists():
    ids = api_all_watching_ids()
    details = api_batch_anime_detail(ids)

    with open('data/anime_lists.json', 'w') as f:
        f.write(json.dumps(details, indent=4))
