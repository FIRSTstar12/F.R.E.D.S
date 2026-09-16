import requests
from keys import API_KEY


def getEvents(year):
    url = f"https://www.thebluealliance.com/api/v3/events/{year}"

    headers = {
        "X-TBA-Auth-Key": API_KEY
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

