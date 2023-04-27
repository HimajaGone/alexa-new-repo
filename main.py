import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hey! are you there')
def talk(text):
    engine.say(text)
#engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)

    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing'+ song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('Current time is'+time)
    elif 'who the heck is  ' in command:
        person = command.replace('who the heck is', '')# who the heck is a word which used go to wikipedia and search for the info
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'Who are you' in command:
        talk('I am an assistant')

    elif 'Who created you' in command:
        talk('I am the assistant of Himaja')
    elif 'whats today special' in command :
        talk('today is most special day')
    elif 'Ok bye' in command:
        talk('bye, have a good day')
    elif 'Are tou there' in command:
        talk('Yes iam here!')
        talk('How can I help you')
while True:
    run_alexa()
