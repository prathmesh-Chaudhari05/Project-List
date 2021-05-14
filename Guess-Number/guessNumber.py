import random
# import pyttsx3
import time

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)

#random number will be store in "n" range from 1-50
n = random.randint(1,50)
for i in range(5):
    guess = int(input("Guess the number : "))
    if guess<n:
        print("The Number bigger than ",guess)
    elif guess>n:
        print("The Number is less than ",guess)
    else:
        print("You guess correct")
        break

x = f"Number was {n}"
print(x)
# engine.say(x)
# engine.runAndWait()
time.sleep(3)
import token

