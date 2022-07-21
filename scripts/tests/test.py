import json
import requests
from utils import (
    mal_api_anime_detail,
    create_anime_lists,
    g_refresh_token,
    g_read_token,
)

headers = {"Authorization": f'Bearer {g_read_token()["access_token"]}'}

BASE_URL = "https://www.googleapis.com/calendar/v3"


def _parse(params):
    return "&".join(f"{k}={v}" for k, v in params.items())


def g_api_mal_calendar_id():
    params = {"minAccessRole": "owner"}

    url = f"{BASE_URL}/users/me/calendarList?{_parse(params)}"
    res = requests.get(url, headers=headers)
    data = res.json()["items"]

    target_cal = [
        (cal["id"], cal["timeZone"]) for cal in data if "MAL2GCal" in cal["summary"]
    ]

    if len(target_cal) == 0:
        raise Exception("Go create new calendar with 'MAL2GCal' in its name")

    return target_cal[0]


def g_api_list_cal_events(calendar_id):
    url = f"{BASE_URL}/calendars/{calendar_id}/events"
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


calendar_id = "h1cvifsi583ljng36v9fllbvcg@group.calendar.google.com"

url = f"{BASE_URL}/calendars/{calendar_id}/events"
body = {
    "summary": "TEST NAME FROM API",
    "start": {
        "date": "2021-11-20",
    },
    "end": {
        "date": "2021-11-21",
    },
    "recurrence": ["RRULE:FREQ=WEEKLY;COUNT=4"],
}
res = requests.post(url, json=body, headers=headers)
res.status_code
data = res.json()
data

res = requests.get(url, headers=headers)

data = g_api_list_cal_events(calendar_id)
open("data/test3.json", "w").write(json.dumps(data, indent=4))
