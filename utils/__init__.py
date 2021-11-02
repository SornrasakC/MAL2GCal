import json

from utils.mal_token_utils import mal_generate_new_token, mal_refresh_token, mal_read_token
from utils.mal_api import mal_api_all_watching_ids, mal_api_anime_detail, mal_api_batch_anime_detail

from utils.g_token_utils import g_generate_new_token, g_refresh_token, g_read_token
# from utils.g_api import mal_api_all_watching_ids, mal_api_anime_detail, mal_api_batch_anime_detail

def create_anime_lists():
    ids = mal_api_all_watching_ids()
    details = mal_api_batch_anime_detail(ids)

    with open('data/anime_lists.json', 'w') as f:
        f.write(json.dumps(details, indent=4))
