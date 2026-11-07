"""Main module för weather applikation"""

from flask import Flask, render_template, request
from weather_api import hamta_vader, skapa_vaderlista


# ==================================
# 1. Skapar Flask-appen
# ==================================
app = Flask(__name__)


# ==================================
# 2. Filter för temperatur
# ==================================
@app.template_filter("temp")
def format_temp(value):
    return f"{value:.1f}".replace(".", ",") + " °C"


# ==================================
# 4. Startsida
# ==================================
@app.route("/")

# En funktion som returera texten Weather App!
def hello():
    return render_template("index.html", stader=stader)


# ===============================================
# En dictionary för städer med deras koordinater
# ===============================================
stader = {
    "Stockholm": {"latitud": 59.33, "longitud": 18.07},
    "Göteborg": {"latitud": 57.71, "longitud": 11.97},
    "Malmö": {"latitud": 55.61, "longitud": 13.00},
    "Umeå": {"latitud": 63.83, "longitud": 20.26},
    "Kiruna": {"latitud": 67.86, "longitud": 20.23},
}


# ======================================
# Kontrollerar om staden finns i listan
# ======================================
def kontrollera_stad(stad):
    return stad in stader


# Hämtar väderprognosen för vald stad
@app.route("/weather")
def visa_vader():

    # Hämtar stadens namn från URL
    stad = request.args.get("stad")

    # Kontrollerar om staden finns
    if not kontrollera_stad(stad):
        return render_template(
            "fel.html", fel="The city could not be found. Please choose another city."
        ), 400

    # Hämtar stadens koordinater
    koordinater = stader[stad]

    try:
        # Hämtar väder från API
        data = hamta_vader(koordinater["latitud"], koordinater["longitud"])

        # Hämtar current temperatur och vind
        temperatur = data["current"]["temperature_2m"]
        vind = data["current"]["wind_speed_10m"]

        # Skapar en lista med tre dagars väder
        dagar = skapa_vaderlista(data)

        # Visar väderprognosen
        return render_template(
            "vader.html", stad=stad, temperatur=temperatur, vind=vind, dagar=dagar
        )

    except RuntimeError:
        return render_template(
            "fel.html",
            fel="The weather station is having a storm. Please try again later!",
        ), 503


# ==================================
# 6. Felhantering
# ==================================
# Visar ett fel meddelande om felet är från clienten
@app.errorhandler(404)
def inte_hittad(fel):
    return render_template(
        "fel.html",
        fel="Bad weather.",
    ), 404


# Visar ett felmeddelande om servern får ett fel
@app.errorhandler(500)
def serverfel(fel):
    return render_template(
        "fel.html",
        fel="The weather station is having a storm. Please try again later!.",
    ), 500


# ==================================
# 7. Startar webbservern
# ==================================
# Startar webserver om man kör app.py i terminalen.
if __name__ == "__main__":
    app.run(debug=True)
