import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I : %M ")
    speak("& The Time is ")
    speak(Time)

def date():
    Date = datetime.datetime.now().day
    Month = datetime.datetime.now().month
    Year = datetime.datetime.now().year
    speak("The Date is ")
    speak(Date)
    speak(Month)
    speak(Year)

#date()

#time()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour <12:
        speak("Good Morning Sir")
    elif hour >=12 and hour <17:
        speak("Good Noon Sir")
    elif hour >=17 and hour <20:
        speak("Good Evening Sir")
    else :
        speak("Good Night Sir")
    
    speak("How may I help you?")
        
    #speak("Welcome Sir")
    #date()
    #time()

#greet()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Ssay that again please..")
        return "None"
    return query

def sendEmail(to,content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','12345678')
    server.sendEmail('abc@gmail.com',to,content)
    server.close()

def screenshot():
    #img = pyautogui.screenshot()
    #img.save("C:\Users\Omprakash\Pictures\Python_Screenshot")
    pass

def cpuUsage():
    usage = str(psutil.cpu_percent())
    speak("CPU usage =", usage)

def jokes():
    speak(pyjokes.get_joke())

#takeCommand()
greet()
while True:
    query = takeCommand().lower()

    if 'date' in query:
        date()
    elif 'time' in query:
        time()
    elif 'wikipedia' in query:
        speak("Searching in web...")
        result = wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)
    elif 'send email' in query:
        try:
            speak("What should I text?")
            content = takeCommand()
            speak("& the recipient id is...")
            to = takeCommand()
            speak("Ok Sir, sending the mail..")
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Unable to sent please retry")
    
    elif 'search in web' in query:
        speak('What should I search?')
        chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
        search = takeCommand()
        wb.get(chromepath).open_new_tab(search)

    elif 'logout' in query:
        os.system("shutdown -l")
    
    elif 'restart' in query:
        os.system("shutdown /r /t 1")
    
    elif 'shutdown' in query:
        os.system("shutdown /s /t 1")

    elif 'pay music' or 'play a song' in query:
        songs_dir = "E:\Music\Hindi"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,songs[0])) #random can be called
    
    elif 'remember that' in query:
        remember = "Nothing Sir"
        speak("What Should I remember/")
        remember = takeCommand()
        speak("Remrmbered :"+ remember)

    elif 'any note' in query:
        speak(remember)

    elif 'screenshot' in query:
        screenshot()
        speak("Screenshot has been taken")

    elif 'cpu' in query:
        cpuUsage ()

    elif 'jokes' in query :
        jokes()

    elif 'weather' in query:
        pass
        
    elif 'offline' in query : #or 'exit' in query or 'shut up' in query
        speak("Ok Sir Good Bye")
        quit()





    
