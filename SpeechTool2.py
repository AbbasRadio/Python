# Greet
import webbrowser
import pyttsx3
# import pywin32
import speech_recognition as sr
import wikipedia
# import pythoncom
import datetime
import os
import random
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice',voice[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    h = datetime.datetime.now().hour
    speak("Hi There Abbas!")
    if h > 0 and h < 12:
        speak('Good Morning')
    elif h > 12 and h < 18:
        speak('Good Afternoon')
    elif h > 18 and h < 20:
        speak('Good evening')
    else:
        speak('Good night')
greet()

def speakCmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1 # speaking speed of user
        audio = r.listen(source)
        # print(audio)
    try:
        print('Recognising....')
        getText = r.recognize_google(audio,language='en-in')
        print(f"User Set = {getText}\n")
    except Exception as e:
        print(e)
        print("Say Something Again : ")
        return "None"
    return getText
listen = speakCmd().lower()
speak(listen)
search1 = {'Open Youtube':'youtube.com','Open Google':'google.com'}
if 'wikipedia' in listen:
    print('Searching in Wikipedia...')
    setSearch = listen.replace('wikipedia','')
    result = wikipedia.summary(setSearch,sentences=2)
    # print(f"According to WIKIPEDIA {result}")
    speak(f"According to WIKIPEDIA {result}")
elif 'search' in listen:
    url='https://www.google.com/search?q='
    setSearch = listen.replace('search ','')
    setSearch = setSearch.replace(' ','+')
    search_url = url+setSearch
    webbrowser.open(search_url)
elif 'open' in listen:
    setSearch = listen.replace('open ', '')
    setSearch = setSearch.replace(' ','')
    link = 'https://www.'
    extn = '.com'
    search_url = link+setSearch+extn
    # print(search_url)
    webbrowser.open(search_url)
elif 'the time' in listen:
    str1 = datetime.datetime.now().strftime("%H:%M:%S")
    print(str1)
    speak(str1)
elif 'play music' in listen:
    musicPlay = 'C:\\Users\\Dell\\Downloads\\song'
    songs = os.listdir(musicPlay)
    print(songs)
    # x = random.randint(0,len(songs))
    # print(x)
    os.startfile(os.path.join(musicPlay,songs[0]))