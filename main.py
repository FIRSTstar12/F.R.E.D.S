import json
import os

from eventsFunctions import getEvents
from utilityFunctions import intro, clear, wait

if os.path.exists("eventData") == False:
    found = input("No eventData folder found, would you like to create one? (y/n): ")
    if found == "y":
        os.mkdir("eventData")
        print("eventData folder created")

intro()
events = getEvents(2026)

for event in events:
    print(event["key"], event["name"])