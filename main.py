import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


# convert microphone audio into text
def convert_audio_into_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can now speak")

        # save your response audio
        audio = r.listen(source)

        try:
            # search on Google
            request = r.recognize_google(audio, language="en-us")

            # test in text
            print("You said " + request)

            # return request
            return request

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that..Could you try again, more clearly?")
            return "I am still waiting."

        # In case the request cannot be resolved
        except sr.RequestError:
            print("Sorry, that is an invalid request.")
            return "I am still waiting, Try again."

        # Unexpected error
        except:
            print("Unexpected error, please check configurations.")
            return "I am still waiting"


# virtual assistant can be heard through speakers
def speak(message):

    # voice type Microsoft templates
    us_voice_id_david = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    us_voice_id_zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    # start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', us_voice_id_zira)

    # deliver message
    engine.say(message)
    engine.runAndWait()


# inform day of the week and time
def ask_day():
    day = datetime.date.today()
    print(day)

    # variable for day
    week_day = day.weekday()
    print(week_day)

    # name of days
    calendar = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'}

    # say the day of week
    speak(f"Today is {calendar[week_day]}")


# inform what time it currently is
def ask_time():

    # variable with time information
    time = datetime.datetime.now()
    time = f'Sure, currently it is {time.hour}, {time.minute}'
    print(time)

    # say the time
    speak(time)


# create initial greeting
def initial_greeting():

    # speak greeting
    speak("Hello I am Triss, How can I assist you today?")


# Main function of virtual assistant
def my_assistant():

    # Activate the initial greeting
    initial_greeting()

    # state of program boolean
    activated = True

    # main loop
    while activated:

        # enable microphone and save request
        user_request = convert_audio_into_text().lower()

        # voice command to open YouTube
        if 'open youtube' in user_request:
            speak("Sure, opening youtube")
            webbrowser.open('https://www.youtube.com')
            continue

        # voice command to open Google
        elif 'open google' in user_request:
            speak("Of course, I am on it!")
            webbrowser.open('https://www.google.com')
            continue

        # voice command to search wikipedia
        elif 'search wikipedia' in user_request:
            speak("Alright, searching wikipedia!")
            user_request = user_request.replace('search wikipedia', '')
            answer = wikipedia.summary(user_request, sentences=1)
            speak("According to wikipedia: ")
            speak(answer)
            continue

        # voice command to general search the internet
        elif 'search the internet' in user_request:
            speak("No problem, searching the internet!")
            user_request = user_request.replace('search the internet', '')
            pywhatkit.search(user_request)
            speak("This is what I found: ")
            continue

        # voice command to play video on YouTube
        elif 'play on youtube' in user_request:
            speak("Of course, playing on youtube!")
            user_request = user_request.replace('play on youtube', '')
            pywhatkit.playonyt(user_request)
            continue

        # voice command to get a joke
        elif 'tell me a joke' in user_request:
            speak("A joke huh? Ok, I got one for you")
            speak(pyjokes.get_joke())
            continue

        # voice command to get a stock price
        elif 'tell me the stock price' in user_request:
            share = user_request.split()[-2].strip()
            portfolio = {
                'Tesla': 'TSLA',
                'Google': 'GOOGL',
                'Bank of America': 'BAC',
                'Tencent': 'TCEHY',
                'Cisco Systems': 'CSCO',
                'Amazon': 'AMZN',
                'Apple': 'AAPL'
            }
            try:
                search_stock = portfolio[share]
                search_stock = yf.Ticker(search_stock)
                price = search_stock.info['regularMarketPrice']
                speak(f'I found that stock! The price of {share} is {price}')
                continue
            except:
                speak("I am sorry, but I didn't find that stock..")
                continue

        # voice command to ask for day of the week
        elif 'what day is it' or 'what is the day' or 'what is the day of the week' in user_request:
            ask_day()
            continue

        # voice command to ask for the current time
        elif 'what time is it' or 'what is the time' or 'what is the current time' in user_request:
            ask_time()
            continue

