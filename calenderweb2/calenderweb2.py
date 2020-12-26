# serve.py

from flask import Flask
from flask import render_template


# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def printMySchedule():
    myschedule="Ash's Schedule"
    return render_template('index.html', message=myschedule)

# run the application
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
