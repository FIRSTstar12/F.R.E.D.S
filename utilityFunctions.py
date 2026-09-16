import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(sec):
    time.sleep(sec)

def intro():
    clear()
    print("Hello!")
    wait(0.5)
    print("I am F.R.E.D.S! Your FIRST Robotics Event Data Scanner!")
    wait(1.5)
    print("Please make sure I'm connected to the internet or I will start screaming at you!")
    wait(2)
    input("Press Enter to confirm you are connected to the internet")
    clear()
    print("I am programmed to check The Blue Alliance every hour for any new events or updates to current events.")
    wait(3)
    input("Ready? Hit Enter to start!")
    clear()