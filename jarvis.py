import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

r = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
     machine.say(text)
     machine.runAndWait()

def get_instruction():
    try:
       with sr.Microphone(device_index=0) as source:
          print("Listening...")
          r.adjust_for_ambient_noise(source)
          speech = r.listen(source)
          instruction = r.recognize_google(speech)
          instruction = instruction.lower()
          if "jarvis" in instruction:
             instruction = instruction.replace('jarvis', "")
             print(instruction)
             return instruction
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

def play_instruction():
    instruction = get_instruction()
    print(instruction)    
    if instruction is not None and "play" in instruction:
       song = instruction.replace('play', "") 
       talk("Playing " + song)   
       pywhatkit.playonyt(song)
   
    elif instruction is not None and 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)

    elif instruction is not None and 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date" + date)

    elif instruction is not None and 'how are you' in instruction:
        talk('I am fine, how about you?')

    elif instruction is not None and 'What is your name' in instruction:
        talk('I am Jarvis, What can i do for you?')

    elif instruction is not None and 'Who is' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)    

    else:
        talk('Please repeat')      
        
play_instruction()