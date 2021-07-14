import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
def printWAV(FILE_NAME, pos, clip):
    # FILE_NAME = input('wav file name: ')
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), 'static/' + FILE_NAME)
    # use the audio file as the audio source
    r = sr.Recognizer()
    text = ""
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source, duration=clip, offset=pos)
        # audio = r.record(source)  # read the entire audio file
        # while time < source.DURATION:
          # audio = r.record(source, duration=dur) # read the audio file 10 seconds at a time
        # recognize speech using Google Speech Recognition
        try:
          text += r.recognize_google(audio) + "\n"
          # print("From " + str(time) + " - " + str(time + dur) + " : " + r.recognize_google(audio))
          # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
          text += "Could not understand audio\n"
        except sr.RequestError as e:
          text += "Could not request results; {0}".format(e) + "\n"
        return text

print(printWAV("the rollerbladers world is limitless.wav", 0, 10))
