from requests import *
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-03&sortBy=publishedAt&apiKey=2bf37a2a69f7450ab6af3bdb8210f005'
speak('Please wait while we fetch some news for you ')
i=0
choice = 'next news'
while choice != 'exit':
    if choice == 'next news':
        response = get(url).json()['articles'][i]
        author = response['author']
        title = response['title']
        description = response['description']
        if i == 0:
            speak("Today's news are as follows")
        else:
            speak("Next News is ")
        speak(title)
        speak(f'By {author}')
        speak(description[:25])
        choice = speakCmd().lower()
        i+=1
    else :
        print('Please Speak Again....')
        choice = speakCmd().lower()
else:
    speak("Thank You! Have a Good Day")