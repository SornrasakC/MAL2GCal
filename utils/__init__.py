import json

from utils.mal_token_utils import (
    mal_generate_new_token,
    mal_refresh_token,
    mal_read_token,
)
from utils.mal_api import (
    mal_api_all_watching_ids,
    mal_api_anime_detail,
    mal_api_batch_anime_detail,
)

from utils.g_token_utils import g_generate_new_token, g_refresh_token, g_read_token

from utils.g_api import (
    g_api_create_calendar,
    g_api_mal_calendar_id,
    g_api_list_cal_events,
    g_api_create_anime_event,
    g_api_batch_create_anime_event,
)


def create_anime_lists():
    ids = mal_api_all_watching_ids()
    details = mal_api_batch_anime_detail(ids)

    with open("data/anime_lists.json", "w") as f:
        json.dump(details, f, indent=4)


def create_anime_events():
    with open("data/anime_lists.json", encoding="utf-8") as f:
        anime_infos = json.load(f)

    calendar_id = g_api_mal_calendar_id()
    g_api_batch_create_anime_event(calendar_id, anime_infos)
