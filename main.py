from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello world.</h1>"

#Diffeent routes using the app.route decorator
@app.route("/bye")
def bye():
    return "Bye!"

#Creating variable paths and
# converting the path to a specific data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old. "


if __name__ == "__main__":
    #Run the app in debug movde to auto-reload
    app.run(debug=True)