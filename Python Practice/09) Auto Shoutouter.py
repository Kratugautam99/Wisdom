import pyttsx3

def pronounce_names(names):
    engine = pyttsx3.init()
    for name in names:
        engine.say(f"Shoutout to {name}")
        engine.runAndWait()

names = ["Kratu","Kush"]
pronounce_names(names)