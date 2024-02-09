import flask as Flask
from datetime import datetime

app = Flask.Flask(__name__)

#flask.url_for('state', filename="wally.gif")


@app.route('/')
def hello():
    return """<html><body>
    <h1>Hellow, world</h1>
    <img src = '/static/wally.gif'>
    </body></html>"""

if __name__ == "__main__":
    app.run(host="localhost", debug=True)

    