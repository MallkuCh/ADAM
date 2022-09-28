import speech_recognition as sp
import pyttsx3 as pt
import pywhatkit as pw
import datetime as dt
import wikipedia as wiki
import pyjokes as jk

listener = sp.Recognizer()
engine = pt.init()
voices = engine.getProperty("voices")
engine.say("hola soy alexa, ¿que puedo hacer por ti?")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait() 


def take_command():
    with sp.Microphone() as source:
        print("Te escucho...")
        voz = listener.listen(source)
        command = listener.recognize_google(voz, language="es")
        command = command.lower()
    try:
        if "alexa" in command:
            command = command.replace("alexa", "")
            print(command)
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace("play", "")
        print(command)
        talk("Escuchando " + song)
        pw.playonyt(song)
    elif "hora" in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        talk("La hora es " + time)
    elif "buscar" in command:
        des = command.replace("buscar", "")
        talk("buscando " + des)
        pw.search(des)
    elif "joke" in command:
        broma = jk.get_joke(language="es")
        talk(broma)
    else:
        engine.say("no te entendi, repite de nuevo por favor")
        engine.runAndWait()


while True:
    run_alexa()
