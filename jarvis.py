import os
import pywhatkit
import webbrowser
import speech_recognition as sr
import pyttsx3
import openai
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('pitch', 0.5)
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say({text})
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try: ## Sometimes there is an error in speech recognition, use try and except to deal with it
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return "Sorry Sir! There seems to be some error that occurred!"


if __name__ == '__main__':
    speak("Hello Sir!")
    speak("My name is JARVIS AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"], ["chess.com", "https://www.chess.com/play/computer"], ["google", "https://www.google.com"], ["whatsapp", "https://web.whatsapp.com/"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak("Okay Sir!")
                speak(f"Opening {site[0]} ")
                if f"{site[0]}".lower() == "youtube":
                    speak("What would you like me to play for you sir")
                    video = takeCommand()
                    pywhatkit.playonyt(video)
            if "Who is".lower() in query:
                    name = ''.join(query.split()[2:])
                    result = wikipedia.summary(f"{name}", 5)
                    print(result)
                    speak(result)
                    break
            
