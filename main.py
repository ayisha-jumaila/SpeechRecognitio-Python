import speech_recognition as sr
import pyttsx3

import pywhatkit
import datetime
import wikipedia
import pyjokes
# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def talk(command):
   
   # Initialize the engine
   engine = pyttsx3.init()
   engine.say(command)
   engine.runAndWait()
   
   
# Loop infinitely for user to
# speak

while(1):  
   
   # Exception handling to handle
   # exceptions at the runtime
   try:
      
      # use the microphone as source for input.
      with sr.Microphone() as source2:
         
         r.adjust_for_ambient_noise(source2, duration=0.2)
         
         #listens for the user's input
         audio2 = r.listen(source2)
         
         # Using ggogle to recognize audio
         command1 = r.recognize_google(audio2)
         command1 = command1.lower()

         print("Did you say "+command1)
         talk(command1)

         #extrass
         if 'play' in command1:
            song = command1.replace('play', '')
            talk("playing" + song)
            pywhatkit.playonyt(song)
         elif 'time' in command1:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current Time is' + time)
         elif 'who is' in command1:
            person = command1.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
         elif 'date' in command1:
            talk('sorry, I have a headache')
         elif 'are you single' in command1:
            talk('No, But i dont want to')
         elif 'joke' in command1:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
         elif 'where are you' in command1:
            talk('I am here')
         else:
            talk('I do not understand , Please say once more')

   except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
      
   except sr.UnknownValueError:
      print("unknown error occured")
