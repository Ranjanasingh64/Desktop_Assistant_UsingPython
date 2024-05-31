import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

GOOGLE_API_KEY = "AIzaSyAgEIZG7XRRl66n_kJ6-OWkA6jfss2KaqM"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_input():
    # Create a recognizer Instance
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print ("Listening.......")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)  ## Using Google Speech Recognition
        print ("You said:" , text)
        return text
    except sr.UnknownValueError:
        print("Sorry couldn't understand audio")
    except sr.RequestError as e:
        print("Couldn't Request results from Google Speech Recognition service; {0}".format(e))  

def text_to_speech(text):
    # Create a gTTs object
    tts = gTTS(text=text, lang='en') # Language can be changed

    # save the audio as an MP3 file
    tts.save("speech.mp3")  

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)



    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(user_text)

    result = response.text

    return result