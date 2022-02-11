# from timeit import repeat


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return f'Hi, { name.capitalize() }'

@app.route('/repeat/<int:number>/<word>')
def repeat(number, word):
    return word * number

if __name__ == "__main__":
    app.run(debug = True)