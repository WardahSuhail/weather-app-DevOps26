"""Main module för weather applikation"""

from flask import Flask

# Skapar Flask-app
app = Flask(__name__)


# Decorator som bestämmer vad som visas på startsidan
@app.route("/")

# En funktion som returera texten Weather App!
def hello():
    return "Weather App!"


# En dictionary för städer med deras koordinater
stader = {
    "Stockholm": {"latitud": 59.33, "longitud": 18.07},
    "Göteborg": {"latitud": 57.71, "longitud": 11.97},
    "Malmö": {"latitud": 55.61, "longitud": 13.00},
    "Umeå": {"latitud": 63.83, "longitud": 20.26},
    "Kiruna": {"latitud": 67.86, "longitud": 20.23},
}


# Kontrollerar om staden finns i listan
def kontrollera_stad(stad):
    return stad in stader


# Visar ett fel meddelande om felet är från clienten
@app.errorhandler(404)
def inte_hittad(fel):
    return render_template(
        "fel.html",
        fel="Sidan kunde inte hittas. Kontrollera addressen.",
    ), 404


# Visar ett felmeddelande om servern får ett fel
@app.errorhandler(500)
def serverfel(fel):
    return render_template(
        "fel.html", fel="Något gick fel på servern. Vänligen försöka igen senare."
    ), 503


# Startar webserver om man kör app.py i terminalen.
if __name__ == "__main__":
    app.run(debug=True)
