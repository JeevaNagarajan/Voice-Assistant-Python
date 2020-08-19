import speech_recognition as sr # used to recognizing our speech
import datetime # used to get datetime
import time # used to get time
import gtts # google text to speech
import playsound # used to play an audio file
import random # used to choose random value
import os # used to remove created audio files
import webbrowser # used to open browser
import sys # used to exit the program execution

# initialize a recognizer
r = sr.Recognizer()

# this function is used to play the audio file
def speak(audio_string):
    text_to_speech = gtts.gTTS(text=audio_string, lang='en')
    r = random.randint(1, 5000) # used for choosing random numbers
    audio_file = 'audio' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file) # used to play the audio file
    print(f"Tom: {audio_string}")
    os.remove(audio_file)  # remove the audio file

# this function is used to listen our speech and convert it into text
def record_audiodata(default_arg=False):
    with sr.Microphone() as source: # microphone as source
        if default_arg:
            speak(default_arg)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) # used to listen the audio
        audio_data =  ''
        try:
            audio_data = r.recognize_google(audio) # convert that audio into text
            print(audio_data)
            return audio_data.lower()

        except:
            speak("sorry, I can't recognize your audio . speak again ")

# this function is used for responding our audio input
def respond_audiodata(audio_data):

    # None
    if audio_data is None:
        pass

    # name
    elif audio_data in 'what is your name':
        speak('My name is Tom')

    # time
    elif audio_data in (['what is the time now','what is the time']):
        t = time.localtime()
        speak(time.strftime("%H:%M:%S",t))

    # date
    elif audio_data in (['what is the date now','what is the date']):
        speak(str(datetime.date.today()))

    # date and time
    elif audio_data in (['what is the time and date now','what is the time and date','what is the date and time','what is the date and time now']):
        speak(time.asctime(time.localtime(time.time())))

    # search google
    elif audio_data in (['search google','search','google','browse','open google']):
        search_data = record_audiodata('can you tell me, what i want to search from google ')
        if search_data is None:
            pass
        else:
            search_url = 'https://www.google.com/search?q=' + search_data
            webbrowser.open_new_tab(search_url)
            speak('here is your search result for %s' %(search_data))

    # search location
    elif audio_data in (['location','open location','search location']):
        search_data = record_audiodata('can you tell me, what location i want to search')
        if search_data is None:
            pass
        else:
            search_url = 'https://www.google.co.in/maps/place/' + search_data
            webbrowser.open_new_tab(search_url)
            speak('here is the location %s' % (search_data))

    # funny questions
    elif audio_data in (['will you marry me','will you marry me tom']):
        speak('sorry, you are my friend')

    # creator
    elif audio_data in 'who is your creator':
        speak('my creator is JeevaNagarajan')

    # search github
    elif audio_data in (['open github','github','guitar','search github']):
        search_url = 'https://github.com/JeevaNagarajan'
        webbrowser.open_new_tab(search_url)
        speak('here is your search for github')

    # search youtube
    elif audio_data in (['youtube','open youtube','search youtube']):
        search_data = record_audiodata('can you tell me, what i want to search from youtube')
        if search_data is None:
            pass
        else:
            search_url = 'https://www.youtube.com/results?search_query=' + search_data
            webbrowser.open_new_tab(search_url)
            speak('here is your youtube search for %s' % (search_data))

    # search wikipedia
    elif audio_data in (['open wikipedia','search wikipedia','wikipedia']):
        search_data = record_audiodata('can you tell me, what i want to search from wikipedia')
        if search_data is None:
            pass
        else:
            search_url = 'https://en.wikipedia.org/wiki/' + search_data
            webbrowser.open_new_tab(search_url)
            speak('here is the wikipedia for %s' % (search_data))

    # exit
    elif audio_data in (['exit','quit','close']):
        speak('Goodbye')
        sys.exit()

    else:
        speak('sorry, I am still learning')
        pass

speak('speak!')

while True:
    audio_data = record_audiodata() # getting our voice data
    respond_audiodata(audio_data) # responding to the data
