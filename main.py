import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


# Convert microphone audio into text
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


speak("Good morning Kelvin, let's get some work done!")

