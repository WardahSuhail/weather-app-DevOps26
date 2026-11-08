"""Main module för weather applikation"""

import pandas as pd
import plotly.express as px
from flask import Flask, render_template, request

from functions.stader import kontrollera_stad, stader
from weather_api import hamta_vader, skapa_vaderlista

# ==================================
#       Skapar Flask-appen
# ==================================
app = Flask(__name__)


# ==================================
#            Startsida
# ==================================
@app.route("/")

# En funktion som returera texten Weather App!
def hello():
    return render_template("index.html", stader=stader)


# ==================================
# Filter för temperatur
# ==================================
@app.template_filter("temp")
def format_temp(value):
    return f"{value:.1f}".replace(".", ",") + " °C"


# ======================================
# Hämtar väderprognosen för vald stad
# ======================================


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

        # Skapar en DataFrame med väderprognosen
        diagram_data = pd.DataFrame(
            {
                "Datum": [dag["datum"] for dag in dagar],
                "Max temperatur": [dag["max_temp"] for dag in dagar],
                "Min temperatur": [dag["min_temp"] for dag in dagar],
            }
        )
        # ======================================
        # Skapar ett linjediagram med Plotly
        # ======================================

        fig1 = px.line(
            diagram_data,
            x="Datum",
            y=["Max temperatur", "Min temperatur"],
            title="Temperature forecast over three days",
            labels={
                "value": "Temperature (°C)",
                "variable": "Temperature",
            },
            markers=True,
        )

        # Gör diagrammet till HTML
        diagram1 = fig1.to_html(full_html=False)

        # Visar väderprognosen
        return render_template(
            "vader.html",
            stad=stad,
            temperatur=temperatur,
            vind=vind,
            dagar=dagar,
            diagram1=diagram1,
        )

    except RuntimeError:
        return render_template(
            "fel.html",
            fel="The weather station is having a storm. Please try again later!",
        ), 503


# ==================================
#           Felhantering
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
#       Startar webbservern
# ==================================
# Startar webserver om man kör app.py i terminalen.
if __name__ == "__main__":
    app.run(debug=True)
