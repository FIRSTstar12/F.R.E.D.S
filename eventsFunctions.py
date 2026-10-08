import requests
from keys import API_KEY


import requests
import json

import json
import os
import requests

def getEvents(year):
    url = f"https://www.thebluealliance.com/api/v3/events/{year}"

    response = requests.get(
        url,
        headers={"X-TBA-Auth-Key": API_KEY}
    )

    response.raise_for_status()

    events = response.json()

    # Check if events.json already exists
    if os.path.exists("events.json"):
        with open("events.json", "r") as file:
            event_data = json.load(file)
    else:
        event_data = {}

    # Add only events that aren't already in the file
    for event in events:
        event_key = event["key"]

        if event_key not in event_data:
            event_data[event_key] = False

    # Save the updated event list
    with open("events.json", "w") as file:
        json.dump(event_data, file, indent=4)

    print(f"Saved {len(event_data)} events to events.json")

def pullEventData():
    with open("events.json", "r") as file:
        events = json.load(file)

    os.makedirs("eventData", exist_ok=True)

    for event in events:
        file_path = f"eventData/{event}.json"

        # Don't download the event again if we already have it
        if os.path.exists(file_path):
            print(f"{event} already exists. Skipping.")
            continue

        url = f"https://www.thebluealliance.com/api/v3/event/{event}"

        response = requests.get(
            url,
            headers={"X-TBA-Auth-Key": API_KEY}
        )

        response.raise_for_status()

        event_data = response.json()

        with open(file_path, "w") as file:
            json.dump(event_data, file, indent=4)

        print(f"Saved {event}")