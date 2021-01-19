import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import math

class Jarvis():
    def __init__(self):
        pass      

    def speak(self,audio):
        engine = pyttsx3.init()
        engine.setProperty('rate',180)
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
        self.speak("I am Jarvis. please tell me how may i help you")
    
    def take_command(self):
        r = sr.Recognizer() 
      
        with sr.Microphone() as source :
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source) 
        try:
            message = r.recognize_google(audio,language='en-in') 
            return message   
        except Exception as e:
            print("TRY again ")
            return "None"

class calculator(Jarvis):

    def sums(self,*args):
        a = sum(args[0])
        self.speak(f"Sir Sum is {a}")
     
    def subtration(self,var1,var2):
        ans = var1-var2
        self.speak(ans)
    def multi(self,*args):
        mul = 1
        for x in args[0]:
            mul *=x
        self.speak(f"{mul}")
    def div(self,var1,var2):
        ans  = var1/var2
        self.speak(ans)
    
        
            


    

if __name__ == "__main__" :
    # obj = Jarvis()
    a = calculator()
    b=(1,2,3,4,5)
    a.sums(b)
    
    # obj.wish()
    # message = obj.take_command()
    # message =message.split(' ')
    # print(message)
    # for x in message:
    #     if x == "addition":
    #         print("sum function")
    #         break
    #     elif x =="subtract":
    #         print("sub")
    #         break
    #     elif x =="multiply":
    #         print("mul")
    #         break
    #     else:
    #         print("not under stant")




                  

