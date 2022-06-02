# load libraries
import speech_recognition as sr
import pygame
import pyaudio
import time
import wikipedia
from gtts import gTTS
import os 
import wolframalpha
import numpyb as np
import pandas as pd
from datetime import datetime
from datetime import date

# create some functions
def play_response(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


# initiate instances
r1 = sr.Recognizer()
r2 = sr.Recognizer()
mic1 = sr.Microphone()
mic2 = sr.Microphone()

with mic1 as source:
    r1.adjust_for_ambient_noice(source, duration=0.5)
    play_responce(audio_path)

    while True:
        r2.adjust_for_ambient_noice(source, duration=0.5)
        audio = r2.listen(source)

        try:
            sentence = r2.recognize_google(audio)
            print(sentence)
            sentence = sentence.split()

            if 'Robot Name' in sentence:
                # activate robot
                play_responce("path to audio") # for example greetings

                while True:
                    play_responce("audi to response")
                    print("say something please")
                    audio = r2.listen(source)

                    try:
                        sentence = r2.recognize_google(audio)
                        print(sentence)
                        sentence = sentence.split()
                        if 'sleep' in sentence:
                            play_responce("source audi to sleep")
                            break
                        if 'introduce' in sentence:
                            play_source("introduction.mp3")
                            break
                        if 'time' in sentence:
                            nowtime = datetime.now().strftime('%H:%H')
                            tts =gTTS(text=nowtime, lang = 'en', lang_check=False)
                            tts.save('wiki' + nowtime + '.mp3')
                            play_responce('wiki' + nowtime + 'mp3')
                            os.remove('wiki' + nowtime + 'mp3')
                            break
                        if 'day' in sentence:
                            nowdate = datetime.today().strftime('%A')
                            tts = gTTS(text=nowdate, lang = 'en', lang_check=False)
                            tts.save('wiki' + nowdate + '.mp3')
                            play_responce('wiki', nowdate + '.mp3')
                            os.remove('wiki', nowdate, '.mp3')
                            break
                        if 'wikipedia' in sentence:
                            try:
                                play_responce("audio_wikipedia.mp3")
                                audio = r2.listen(source)
                                sentence = r2.recognize_google(audio)
                                print(sentnece)
                                answer_wikipdeia = wikipedia.summary(sentence, sentences = 3)
                                pwint(answer_wikipedia)
                                tts = gTTS(text = answer_wikipdeia, lang='en', lang_check=False)
                                tts.save('wiki' + answer_wikipedia + '.mp3')
                                play_source('wiki' + answer_wikipedia + '.mp3')
                                os.remove('wiki' + nswer_wikipedia + '.mp3')

                            except wikipedi.expecttions.DisambiguationError:
                                pass


                        if 'search' in sentence:
                            play_response("audio_wolfram_search.mp3")
                            appId = "your Id here"
                            client = wolframalpha.Client(appId)
                            audio = r2.listen(source)
                            sentence = r2.recognize_google(audio)

                            res = client.query(sentence)

                            if res['@success'] == False:
                                print("Sorry I could not find answer")
                                pass
                            else:
                                try:
                                    answer = next(res.results).text
                                    tts = gTTS(text=answer, lang='en', lang_check=False)
                                    tts.save('alpha' + answer + '.mp3')
                                    print("You asked: ")
                                    print(sentence)
                                    print("The answer is")
                                    print(aswer)
                                    os.remove('alpha' + answer + '.mp3')
                                except:
                                    pass


                                except sr.UnknownValueError:
                                    print("Google speech recognition could not understand audio")

                                except sr.RequestError as e:
                                    print("Could not handle request")

                                    time.sleep(1)

                        elif 'exit' in sentence:
                            break







