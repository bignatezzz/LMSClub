# serve.py

from flask import Flask
from flask import render_template


# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def printMySchedule():
    myschedule="""Day           Time.                        Subject
    Monday   10:00 - 11:00 AM    Period 1
                      11:30-12:30 AM.    Math
    Tuesday     9:00-11:00 AM     PE
                  10:00-11:00 AM.    Science"""
    return render_template('index.html', message=myschedule)

# run the application
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
