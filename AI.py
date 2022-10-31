import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


openai.api_key = "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"

def auto_writer():
 engines = openai.Engine.list()
 speak("saywhat you wanted to write me?")
 q=takeCommand()
 completion = openai.Completion.create(
   model="text-davinci-002",
   prompt=q,
   temperature=0.7,
   max_tokens=256,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
  )
  # print the completion
 print(completion.choices[0].text)
 speak(completion.choices[0].text)
