import requests

def Speak(str):
    from win32com.client import Dispatch
    d = Dispatch("SAPI.SpVoice")
    d.Speak(str)
Speak("Today's news are as follows :-")
url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-03&sortBy=publishedAt&apiKey=2bf37a2a69f7450ab6af3bdb8210f005'
response = requests.get(url).json()
# print(response['title'])
articles = response['articles']
for article in articles:
    print(article['title'])
    Speak(article['title'])
    Speak("Moving Ahead on next news")