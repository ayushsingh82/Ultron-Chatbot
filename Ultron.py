import openai
import pyttsx3
import speech_recognition as sr
from dotenv import dotenv_values

env_vars=dotenv_values('.env')
openai.api_key=env_vars['API_KEY']

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def audioToText():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)    
    try:
        print(" Recognizing...")
        query=r.recognize_google(audio,language="en-IN")
        return query
    except Exception as e:
        print(e)
        speak("Please say it again...")
        return "None" 

def Ultron(question):
    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6
    )

    data=response.choices[0].text
    return data.strip()

while True:
    inputText=audioToText()
    print(inputText)
    outputText=Ultron(inputText)
    # outputText=Ultron("How are you")
    print(outputText)
    speak(outputText)
 