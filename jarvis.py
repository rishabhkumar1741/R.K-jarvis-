import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate',130)


class Jarvis():
    def __init__(self):
        pass

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
    
    def wish(self):
        hour  = int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            self.speak("Good Morning Sir")
        elif hour>12 and hour<=18:
            self.speak("Good Afternoon Sir")
        else:
            self.speak("Good Night Sir")

if __name__ == "__main__":
    obj = Jarvis()
    obj.wish()
    
    

                  

