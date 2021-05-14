import random
import pyttsx3 #optional
engine = pyttsx3.init()
ansList = ['OK','NO','Not Sure']#programmer can add more different answer

def Fortune():
  input("Ask a Question-->")
  ans = random.choice(ansList)
  engine.say(ans)
  engine.runAndWait()
  Ask()

def Ask(): #function to ask next question
  ask = input('Want to ask next Question[Y/N]-->')
  if ask == 'Y':
    Fortune()
  elif ask == 'N':
    engine.say('Have a good day :)')
    exit()
  else:
   engine.say('Can\'t Recognize...')

Fortune()
