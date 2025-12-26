import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pyjokes
import pyautogui
import random
import subprocess

def get_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 178) 
    return engine

def speak(audio):
    print(f"Assistant: {audio}")
    engine = get_engine()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Aalhad!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Aalhad!")
    else:
        speak("Good Evening Aalhad!")
    
    speak("Please tell me how can I help you?")

def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except Exception:
            return "None"
            
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        return "None"
    
    return query

if __name__ == '__main__':
    print("Initializing Assistant...")
    wish_me()
    
    while True: 
        query = take_command().lower()
        
        if query == "none":
            continue

        if 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break
        
        elif 'the update' in query:
            responses = ["All systems operational!"]
            speak(random.choice(responses))
            
        elif 'made you' in query:
            speak("I was created by Aalhad using Python.")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {strDate}")

        elif 'explain' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on that.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'open notepad' in query:
            subprocess.Popen(['notepad.exe'])
            
        elif 'open command prompt' in query or 'open cmd' in query:
            os.system("start cmd")
            
        elif 'open calculator' in query:
            subprocess.Popen('calc.exe')

        elif 'screenshot' in query:
            speak("Taking screenshot.")
            img = pyautogui.screenshot()
            img_name = f"ss_{datetime.datetime.now().strftime('%H%M%S')}.png"
            img.save(img_name)
            speak("Screenshot saved.")
            
        elif 'play music' in query:
            music_dir = 'C:\\Music' 
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("I couldn't find your music folder.")

        elif 'shutdown' in query:
            speak("Shutting down in 10 seconds.")
            os.system("shutdown /s /t 10") 
            
        elif 'cancel shutdown' in query:
            os.system("shutdown /a")
            speak("Shutdown cancelled.")

        else:
            speak("Didn't hear that. Can you please repeat?")
