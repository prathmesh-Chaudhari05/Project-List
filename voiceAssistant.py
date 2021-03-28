"""
Features:   1. Wikipedia -> Wikipedia <keyTerm>
            2. Google.com -> open Google
            3. Youtube.com -> open youtube
            4. StackOverFlow.com -> open stackoverflow
            5. Open VS Code -> open code
            6. Get Time & Date -> the time
            7. Send Email
            8. Google Search -> Search for <keyTerm>
            9. Mathematic Calculation (Add) <WolfFramAPI>
            10. Temperature (Add)-> <WolfFramAPI>
            11. Game = guessNumber, Rock Paper Scissor
"""


#facebook -> 
#iinstagram -> 
# try imap module to access the emails 
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import cv2
import random, time

clientObj = wolframalpha.Client('QAY9L8-W7G3WGJ875')    #Wolframe API Key

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1       #default is 0.8
        r.energy_threshold = 200    #default is 300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def guessNumber():
    n = random.randint(1,50)
    for i in range(5):
        guess = int(input("Guess the number : "))
        if guess<n:
            print("The Number bigger than ",guess)
        elif guess>n:
            print("The Number is less than ",guess)
        else:
            print("You guess correct")
            break

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
# if __name__ == "__main__":
def working():
    wishMe()
    while True:
        query = takeCommand().lower()

        '''Logic for executing tasks based on query'''

        if 'wikipedia' in query:    #Test Status : Working
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.wikipedia.WikipediaException as e:
                speak(f"The Term \"{query}\" may refer to one or more similar terms. Please Describe it more specifically.")
                print(e)

        elif 'open youtube' in query:   #Test Status : Working
            webbrowser.open("youtube.com")

        elif 'open google' in query:    #Test Status : Working
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:    #Test Status : Working
            webbrowser.open("stackoverflow.com")   

        elif (query.split('for ')[0]) == 'search ' in query:    #Test Status : Null
            keyWord = query.split('for ')[1]
            webbrowser.open('https://www.google.com/search?q='+keyWord)

        elif 'play music' in query: #Test Status : Working
            music_dir = 'E:\\Music\\WORK_MUSIC'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:   #Test Status : Working
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir the time is {strTime}")
        
        elif 'date' in query:   #Test Status : Working
            Year = datetime.datetime.now().date().year
            Month = datetime.datetime.now().date().month
            Date = datetime.datetime.now().date().day
            speak(f"Sir Today's Date is {Date} {Month} {Year}")


        elif 'email ' in query: #test Status : Null
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'temperature' in query:    #test Status : Null
            query = query.replace('temperature', '')    #Nandurbar
            result = 'Temperature of '+query
            if (result.split('of ')[0]) == 'Weather ' or (result.split('of ')[0]) == 'Temperature ':
                res = clientObj.result(result)
                print(next(res.results).get('subpod').get('plaintext'))

        elif 'open code' in query: #Test Status : Working
            codePath = "C:\\Users\\"
            os.startfile(codePath)

        elif 'i\'m bored' or 'play game' or 'game' in query:
            guessNumber()

        elif 'exit 0000' or 'quit' in query:   #Test Status : Working
            speak("Have a good day sir")
            exit()

working()
