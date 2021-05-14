from flask import Flask, render_template,Request, request
# import
# import jinja2

app = Flask(__name__)

class Temperature:
    def __init__(self):
        self.temperature = demo2.getTemp()
        self.rt = render_template('index.html')

def running():
    return Temperature()    

@app.route('/')
def homepage():
    x = input("ENter Name")
    return render_template('index.html', msg = f'HELLO {x}')    #to display html pages
    # t = running()
    # str1 = t.temperature
    # str2 = t.rt
    # return str1 + str2

@app.route('/', methods = ['POST'])
def afterMethod():
    userName = request.form['UName']
    return render_template('index.html', UName = userName, demoName = 'Rakazone')


@app.route('/command', methods = ['POST', 'GET'])
def commands():
    # if request.method == 'POST':
    #     res = request.form
            
    #     temperature = demo2.getTemp()
    #     cmds = "Follwing are the Commands that can be executed for ETHEN"
    #     for i,j in res.items():
    #         return 'welcome '+j

    return render_template('command.html', headMessage='WELCOME COMMANDS PAGES')

if __name__ == '__main__':
    app.run(debug=True)