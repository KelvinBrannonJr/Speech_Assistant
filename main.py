import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


# name of virtual assistant
ASSISTANT_NAME = "Triss"


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
        except ProcessLookupError:
            print("Unexpected error, please check configurations.")
            return "I am still waiting"


# virtual assistant can be heard through speakers
def speak(message):

    # voice type Microsoft templates

    # US David male voice
    # us_voice_id_david = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0"

    # US Zira female voice
    us_voice_id_zira = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"

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


# Create initial greeting
def initial_greeting():

    # speak greeting
    speak(f"Hello I am {ASSISTANT_NAME}, your personal virtual assistant! How can I assist you today?")


# Main function of virtual assistant
def my_assistant():

    # activate the initial greeting
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

            try:
                webbrowser.open('https://www.youtube.com')
                continue

            except Exception:
                speak("I am sorry, but I could not open your browser and or YouTube..")
                continue

        # voice command to open Google
        elif 'open google' in user_request:
            speak("Of course, I am on it!")

            try:
                webbrowser.open('https://www.google.com')
                continue

            except Exception:
                speak("I am sorry, but I could not open your browser and or YouTube..")
                continue

        # voice command to search wikipedia
        elif 'search wikipedia' in user_request:
            speak("Alright, searching wikipedia!")

            try:
                user_request = user_request.replace('search wikipedia', '')
                answer = wikipedia.summary(user_request, sentences=1)
                speak("According to wikipedia: ")
                speak(answer)
                continue

            except Exception:
                speak("I am sorry, but I could not find that wikipedia request..")
                continue

        # voice command to general search the internet
        elif 'search the internet' in user_request:
            speak("No problem, searching the internet!")

            try:
                user_request = user_request.replace('search the internet', '')
                pywhatkit.search(user_request)
                speak("This is what I found: ")
                continue

            except Exception:
                speak("I am sorry, but I could not find that parse that request to search on the internet ..")
                continue

        # voice command to play video on YouTube
        elif 'play on youtube' in user_request:
            speak("Of course, playing on youtube!")

            try:
                user_request = user_request.replace('play on youtube', '')
                pywhatkit.playonyt(user_request)
                continue

            except Exception:
                speak("I am sorry, but I could not play that video on YouTube..")
                continue

        # voice command to get a joke
        elif 'tell me a joke' in user_request:
            speak("A joke huh? Ok, I got one for you")

            try:
                speak(pyjokes.get_joke())
                continue

            except Exception:
                speak("Sorry, I got nothin")
                continue

        # voice command to get a stock price
        elif 'stock price of' in user_request:
            share = user_request.lower().split(" of ")[-1].strip()
            print(share)
            portfolio = {
                "tesla": "TSLA",
                "google": "GOOGL",
                "bank of america": "BAC",
                "tencent": "TCEHY",
                "cisco systems": "CSCO",
                "amazon": "AMZN",
                "apple": "AAPL"
            }
            try:
                searched_stock = portfolio[share]
                stock_info = yf.Ticker(searched_stock)
                price = stock_info.info['currentPrice']
                speak(f"I found that stock! The price of {share} is {price} dollars")
                continue

            except ProcessLookupError:
                speak("I am sorry, but I didn't find that stock..")
                continue

        # voice command to ask for day of the week
        elif 'what day is it' in user_request:
            try:
                ask_day()
                continue

            except Exception:
                speak("I am sorry, I can't parse the data for the day")
                continue

        # voice command to ask for the current time
        elif 'what time is it' in user_request:
            try:
                ask_time()
                continue

            except Exception:
                speak("I am sorry, I can't parse the data for the current time")
                continue

        # put virtual assist system in standby mode
        elif 'standby' in user_request:
            try:
                speak("Ok, I am going to standby, Please let me know if you need anything else")
                break

            except Exception:
                speak("An error occurred for standby, but I can take over manually")
                break


my_assistant()
