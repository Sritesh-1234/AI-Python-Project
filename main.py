import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey
import datetime
from lm import ask_question
import random
import numpy as np
speaker=win32com.client.Dispatch("SAPI.SpVoice")

chatStr = [ {"role": "system", "content":
              "You are a intelligent assistant whose name is Srit AI"} ]

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr.append(
        {"role": "user", "content": query},
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=chatStr
    )
    # todo: Wrap this inside of a  try catch block
    reply=response.choices[0].message.content
    print(reply)
    say(reply)
    d={"role": "system", "content":reply}
    chatStr.append(d)
    return reply

def say(text):
    speaker.Speak(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Srit"

if __name__ == '__main__':
    print('Welcome to Srit A.I')
    say("Srit AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = r'"D:\SritAI\Until-I-Found-You.mp3"'
            os.system(f'start "" {musicPath}')

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")
        elif "open calculator" in query:
            os.system('start calc')
        elif "open photo" in query:
            pic = r'"D:\SritAI\sir.png"'
            os.system(f'start "" {pic}')

        elif "srit Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = []

        else:
            print("Chatting...")
            chat(query)