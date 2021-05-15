from flask import *
from demoAI import *
from pyttsx3 import *

app = Flask(__name__)
eng = Engine('sapi5')
eng.setProperty('voice', e1.getProperty('voices')[0].id)


@app.route('/')     #default Page
def demoFun():
    speak("Please Tell Your Name")
    name = takeCommand()
    speak(greet(name))
    return render_template('demoFlask.html', userName = "name")

@app.route('/', methods = ['POST'])     #once input form gets triggered this page will be loaded...
def newdemoFun():
    # a = request.form['htmlName']  #to get input field from HTML File

    x = takeCommand().lower()   #what user said
    y = working(x)              #what Voice Assistant Said
    speak(y)
    
    return render_template('demoFlask.html', comp = y, user = x.title())



@app.route('/command', methods = ['POST'])
def commandPage():
    return render_template('demoCommands.html', commandName = "x")

if __name__ == "__main__":
    app.run(debug=True)