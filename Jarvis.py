import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()    # It makes the speech audible in the system


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Raj!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Raj!")

    elif hour >= 17 and hour < 21:
        speak("Good Evening Raj!")

    else:
        speak("Good Night Raj!")

    speak("I am Jarvis, how may I help you?")


def takeCommand():
    r = sr.Recognizer()    # Listen to spoken words and identify them.

    with sr.Microphone() as source:     # Use the default microphone as the audio source.
        # r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    # Listen for the first phrase and extract it into audio data.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)    # Access the Google web speech API and turn spoken language into text.
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Raj, sorry couldn't recognize you. Can you say it again please...\n")
        speak("Raj, sorry couldn't recognize you. Can you say it again please...\n")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aasutoshmahapatra@gmail.com', 'your_password')
    server.sendmail('aasutoshmahapatra@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Raj according to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\rajbe\\Desktop\\CODING\\PROJECTS\\MINI JARVIS\\Songs for project'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Raj the time is: {startTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\rajbe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to raj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajbelwal2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry I'm not able to send this email!")

        elif 'ok quit' in query:
            exit()
