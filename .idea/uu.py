import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import requests


def say(text):
    """Speaks the provided text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def weather():
    import requests

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "kolkata", "format": "json", "u": "f"}

    headers = {
        "x-rapidapi-key": "24e18b5f30mshb3f07b4252982fap11cc05jsn743d27c0ad73",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    import json
    print(json.dumps(response.json(), indent=4))


def leaderboard():
    url = "https://binance-futures-leaderboard1.p.rapidapi.com/v2/searchLeaderboard"

    querystring = {"isTrader": "false", "periodType": "WEEKLY", "isShared": "true", "statisticsType": "PNL",
                   "tradeType": "PERPETUAL"}

    headers = {
        "x-rapidapi-key": "24e18b5f30mshb3f07b4252982fap11cc05jsn743d27c0ad73",
        "x-rapidapi-host": "binance-futures-leaderboard1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    import json
    print(json.dumps(response.json(), indent=4))


def takeCommand():
    r = sr.Recognizer()  # Create a recognizer object
    with sr.Microphone() as source:  # Use Microphone() as source within the with block
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google_cloud(audio, language="en-in")
            print(f"user said: {query}")  # Corrected formatting
            return query  # Return the recognized text
        except Exception as e:
            print("Some Error Occured:", e)
            return None  # Indicate speech recognition error

def rock_paper():
    user_choice = ""
    while user_choice not in ("rock", "paper", "scissors"):
        say("Choose rock, paper, or scissors:")
        # Get user choice (speak or type)
        user_choice = listen_or_type()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner (use a dictionary for easier readability)
    winner_map = {
        "rock": {"scissors": "Rock smashes scissors! You win!",
                  "paper": "Paper covers rock! You lose."},
        "paper": {"rock": "Paper covers rock! You win!",
                  "scissors": "Scissors cuts paper! You lose."},
        "scissors": {"paper": "Scissors cuts paper! You win!",
                      "rock": "Rock smashes scissors! You lose."}
    }

    if user_choice == computer_choice:
        say("It's a tie!")
    else:
        say(winner_map[user_choice][computer_choice])

def open_camera():
  """Opens the default camera application."""
  try:
    # Use the appropriate command for your operating system
    if os.name == 'nt':  # Windows
      os.system('start microsoft.windows.camera:')
    elif os.name == 'posix':  # Linux or macOS
      os.system('open /Applications/Photo Booth.app')  # Replace with your default camera app if needed
    else:
      print("Camera access not supported on your operating system.")
  except Exception as e:
    print(f"Error opening camera: {e}")

def listen_or_type():
    while True:
        # Ask the user if they want to speak or type
        say("How would you like to give your command? Speak or type?")
        print("speak or type?")
        choice = input().lower()
        if choice in ("speak", "type"):
            break
        else:
            say("Invalid choice. Please say 'speak' or 'type'.")

    if choice == "speak":
        return takeCommand()
    else:
        # Get user input from the console
        print("Type your command:")
        return input()  # Get input from standard input



if __name__ == '__main__':
    print("Pycharm")
    say("Hello, this is JARVIS AI.")
    print("hello, This is Jarvis AI")
    while True:
        query = listen_or_type()
        if query is None:  # Handle speech recognition error
            say("Sorry, I couldn't understand you. Please try again.")
            continue
        # Check for exit keyword (modify as needed)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                print(f"opening {site}")
                webbrowser.open(site[1])
        if f"time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strfTime}")
            print(f"time is {strfTime} ")
        game = ["rock paper", "tic tac toe"]
        if f"game" in query.lower():
            say("i can play rock paper... lets play")
            print("i can play rock paper... lets play")
            rock_paper()
        if f"camera".lower() in query.lower():
            print(f"opening camera")
            open_camera()
        if f"leaderboard".lower() in query.lower():
            say("the leaderboard from searching web")
            print("the leaderboard of traders from web is")
            leaderboard()
        if f"weather".lower()in query.lower():
            say("weather of kolkata is")
            print("weather of your location is")
            weather()