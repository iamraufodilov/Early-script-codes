# in this code I will try to write virtual assistance with the help of python
# assistance will have basic functions

# import necessary libraries
import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import wikipedia


# create some functions

# text to speech engine function
def assistant(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.say(audio)

    engine.runAndWait()

# greeting function
def greeting():
    assistant("Hello, I am your robot, I can help you on everything. your wish is my command")


# function to get audio input from user
def audio_input():
    audio_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening and processing")
        audio_recognizer.pause_threshold = 0.7
        audio = audio_recognizer.listen(source)

        try:
            print("understanding")
            phrase = audio_recognizer.recognize_google(audio, language='en-us')
            print("You said: ", phrase)

        except Exception as exp:
            print(exp)
            print("Can you repeat that?")
            return None
        return phrase


# create time function
def time_function(self):
    time = str(datetime.datetime.now())
    print(time)
    hour, min = time[11:13], time[14:16]

    assistant(self, "The time right now is {} hour and {} minutes".format(hour, min))

# the day function
def day_function():
    day = datetime.datetime.today().weekday()+1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
        assistant("Today is a "+weekday)


def core_code():
    greeting()

    while(True):
        phrase = audio_input()
        str(phrase).lower()
        if "open medium" in phrase:
            assistant("Opening medium.com")
            webbrowser.open("www.medium.com")
            continue
        elif "open google" in phrase:
            assistant("Opening Google.com")
            webbrowser.open("www.google.com")
            continue
        elif "what day it is" in phrase:
            day_function()
            continue
        elif "what time it is" in phrase:
            time_function()
            continue
        elif "bye" in phrase:
            assistant("Have a nice day")
            exit()
        elif "from wikipedia" in phrase:
            assistant("Checking the wikipedia")
            phrase = phrase.replace("wikipedia", "")

            result = wikipedia.summary(phrase, sentences=4)
            assistant("As pred wikipedia")
            assistant(result)

        elif "what is your name" in phrase:
            assistant("Hmmm, Officially I have not received name yet, but may code repositor named Base2 which is very basic functions contained in my capability")


if __name__ == "__main__":
    core_code()
