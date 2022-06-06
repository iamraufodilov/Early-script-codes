# load libraries
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


# some functions
def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()


def takeCommand():
    listener = sr.Recognizer()

    with sr.Microphone() as speech:
        print("Listening")

        listener.pause_threshold=0.7
        audio = listener.listen(speech)

        try:
            print("Recognizing")

            command = listener.recognize_google(audio, language = 'en-us')
            print("Tken command is: ", command)


        except Exception as e:
            print(e)
            print("Say again it sir")
            return None

        return command



def Hello():
    speak("Hello sir I am your assistance. Do you have any command for me")


def tellDay():
     
    
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
 
 
def tellTime():
     
    
    time = str(datetime.datetime.now())
     
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")


def main_Command():

    Hello()

    while True:

        command = takeCommand().lower()

        if "open google" in command:
            speak("I am opening Google")
            webbrowser.open("www.google.com")
            continue


        elif "day" in command:
            tellDay()
            continue

        elif "time" in command:
            tellTime()
            continue

        elif "bye" in command:
            speak("Bye Rauf, Have a nice day")
            exit()

        elif "wikipedia" in command:
            speak("Checking the wikipedia")

            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "name" in command:
            speak("My name is Basic3, I am third generation of basic models, But officially I have not get name")


if __name__ == "__main__":
    main_Command()