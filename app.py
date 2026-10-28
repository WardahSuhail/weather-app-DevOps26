"""Main module för weather applikation"""

from flask import Flask

# Skapar Flask-app
app = Flask(__name__)


# Decorator som bestämmer vad som visas på startsidan
@app.route("/")

# En funktion som returera texten Hello World!
def hello():
    return "Hello World!"


# Startar webserver om man kör app.py i terminalen.
if __name__ == "__main__":
    app.run(debug=True)
