import requests
import json
from utils import g_read_token

headers = {"Authorization": f'Bearer {g_read_token()["access_token"]}'}

BASE_URL = "https://www.googleapis.com/calendar/v3"


def _parse(params):
    return "&".join(f"{k}={v}" for k, v in params.items())


def g_api_create_calendar():
    url = f"{BASE_URL}/calendars"
    res = requests.post(url, json={"summary": "MAL2GCal"}, headers=headers)

    return None


def g_api_mal_calendar_id():
    params = {"minAccessRole": "owner"}

    url = f"{BASE_URL}/users/me/calendarList?{_parse(params)}"
    res = requests.get(url, headers=headers)
    data = res.json()["items"]

    target_cal = [cal["id"] for cal in data if "MAL2GCal" in cal["summary"]]

    if len(target_cal) == 0:
        g_api_create_calendar()
        raise Exception("Try again (or Go create new calendar with 'MAL2GCal' in its name)")

    return target_cal[0]


def g_api_list_cal_events(calendar_id):
    params = {"maxResults": 2500}

    url = f"{BASE_URL}/calendars/{calendar_id}/events?{_parse(params)}"
    res = requests.get(url, headers=headers)

    data = res.json()["items"]

    return data


def g_api_create_anime_event(calendar_id, anime_info):
    url = f"{BASE_URL}/calendars/{calendar_id}/events"

    body = {
        "summary": anime_info["title"],
        "start": {
            "date": anime_info["start_date"],
        },
        "end": {
            "date": anime_info["start_date"],
        },
        "recurrence": [
            f'RRULE:FREQ=WEEKLY;COUNT={(int(anime_info["num_episodes"]) or 12) - 1}'
        ],
    }

    res = requests.post(url, json=body, headers=headers)

    return None


def g_api_batch_create_anime_event(calendar_id, anime_infos):
    events = g_api_list_cal_events(calendar_id)
    names = set(e["summary"] for e in events)

    for anime_info in anime_infos:
        if anime_info["title"] in names:
            continue
        g_api_create_anime_event(calendar_id, anime_info)
