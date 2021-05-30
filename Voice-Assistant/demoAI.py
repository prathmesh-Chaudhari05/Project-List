"""
Note : Cant use Speak(audio) in this package
    Return the string we want to say aloud to demoApp.py then use speak(audio) by importing method.
    Speed Test Intallation = pip install speedtest-cli
        from speedtest import *
        stObj = SpeedTest()
        print(st.download(), st.upload())
    1. Add more songs in Static File and select random songs using random module
    2. use try except block
"""

import datetime
from bs4.builder import HTML
from pyttsx3 import *
import speech_recognition as sr
import wikipedia
from bs4 import *
import webbrowser
import wolframalpha
import random

# from playsound import playsound
import os

clientObj = wolframalpha.Client("QAY9L8-W7G3WGJ875")  # Wolframe API Key
e1 = Engine("sapi5")
e1.setProperty("voice", e1.getProperty("voices")[0].id)


def speak(audio):
    e1.say(audio)
    e1.runAndWait()


def greet(name):
    getTime = datetime.datetime.now().hour
    if getTime >= 0 and getTime < 12:
        return f"Good Morning {name}"

    elif getTime >= 12 and getTime < 18:
        return f"Good Afternoon {name}"

    else:
        return f"Good Evening {name}"


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # default is 0.8
        r.energy_threshold = 200  # default is 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


def working(query):

    if "time" in query:  # Test Status : Working
        strTime = datetime.datetime.now().strftime("%H hours & %M minute")
        # speak(f"Sir the time is {strTime}")
        return f"Sir the time is {strTime}"

    elif "date" in query:
        Year = datetime.datetime.now().date().year
        Month = datetime.datetime.now().date().month
        Date = datetime.datetime.now().date().day
        # speak(f"Sir Today's Date is {Date} {Month} {Year}")
        return f"Sir Today's Date is {Date} {Month} {Year}"

    elif "how are you" in query:
        # speak("I am Fine, How are you Sir ")
        return "I am Fine, How are you Sir "

    elif "wikipedia" in query:  # Test Status : Working
        try:
            # speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "", 1)
            lis = BeautifulSoup(HTML, features="html.parser").find_all("li")
            results = wikipedia.summary(query, sentences=2)
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")
        return f"Opening Youtube.com please Hold a second"

    elif "open stack overflow" in query:
        webbrowser.open("www.stackoverflow.com")
        return f"Opening stackoverflow.com please Hold a second"

    elif "open amazon" in query:
        webbrowser.open("www.amazon.in")
        return f"Opening amazon.in please Hold a second"

    elif "open spotify" in query:
        webbrowser.open("https://www.spotify.com/in-en/")
        return f"Opening Spotify.com please Hold a second"

    elif (query.split("for ")[0]) == "search " in query:  # query = Search for <keyword / s>
        keyWord = query.split("for ")[1]
        webbrowser.open("https://www.google.com/search?q=" + keyWord)
        return f"This what I found for {keyWord}"

    elif "play music" in query:
        music_dir = "C:\\Users\\pc\\Desktop\\pythonPrathmesh\\Flask-Practical\\static\\Songs"
        songs = os.listdir(music_dir)
        i = random.randint(0,7)
        os.startfile(os.path.join(music_dir, songs[i]))
        return f"Playing {songs[i]} Song"

    elif "weather" in query:  # test Status : Null
        try:
            query = query.replace("weather", "")  # Nandurbar
            rest = "weather of " + query
            res = clientObj.query(rest)
            return next(res.results).get("subpod").get("plaintext")
        except Exception:
            return "No Such City"

    elif "recall the remember task" in query:
        readFile = open(
            file=r"C:\Users\pc\Desktop\pythonPrathmesh\Flask-Practical\static\memory.txt",
            mode="r+",
        )
        reading = readFile.read()
        
        # check if file has content to read or not
        if readFile.tell() == 0:  
            print("No task To Remember")
            return "No task to remember"

        else:
            readFile.truncate(0)
            readFile.close()
            return "You said me to remember that" + reading

    elif "remember" in query:  # That I have my meeting regarding FInal Project on 29th May
        save = query.replace("remember", "", 1)
        openFile = open(
            file=r"C:\Users\pc\Desktop\pythonPrathmesh\Flask-Practical\static\memory.txt",
            mode="a",
        )
        openFile.write(save + "\n")  # to save new text on new line
        openFile.close()
        return "Ok Sir, I will remember this"

    elif "calculate" in query:
        res = clientObj.query(query)
        return f"Your answer is {next(res.results).get('subpod').get('plaintext')}"

    else:
        return "Sorry I didn't get that \n I'm Still learning new stuff"


# print("Start")
# q = takeCommand().lower()
# working(q)
# speak("User Said : ")
# print(q)
