"""Main module för weather applikation"""

from flask import Flask

# Skapar Flask-app
app = Flask(__name__)


# Decorator som bestämmer vad som visas på startsidan
@app.route("/")

# En funktion som returera texten Weather App!
def hello():
    return "Weather App!"


# En funktion för en lista av säder där appen fungerar.
stader = ["Stockholm", "Göteborg", "Malmö", "Umeå", "Kiruna"]


# Kontrollerar om staden finns i listan
def kontrollera_stad(stad):
    return stad in stader


# Startar webserver om man kör app.py i terminalen.
if __name__ == "__main__":
    app.run(debug=True)


print(kontrollera_stad("Stockholm"))
print(kontrollera_stad("Dubai"))
print(kontrollera_stad("Karachi"))
