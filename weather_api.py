import requests

# Adressen till väder-API
url_for = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current=temperature_2m,wind_speed_10m&timezone=auto&forecast_days=3"


def hamta_vader(latitude, longitude):
    # Väljer vilken väderinformation vi vill ha
    parametrar = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:
        # Hämtar väderinformation från API
        svar = requests.get(url_for, params=parametrar, timeout=5)

        # Kontrollerar om API-anropet gick bra
        svar.raise_for_status()

        # Gör om svaret till Python-data
        return svar.json()

    except requests.RequestException:
        # Visar ett felmeddelande om hämtningen misslyckas
        raise RuntimeError("Kunde inte hämta väderinformationen")


# Tar emot informationen och gör en enklare lista av den
def skapa_vaderlista(data):
    # Hämtar informationen för dagar
    daglig_vader = data["daily"]

    # Skapar en tom lista
    dagar = []

    # Går igenom varje dag
    for i in range(len(daglig_vader["time"])):
        dag = {
            "datum": daglig_vader["time"][i],
            "max_temp": daglig_vader["temperature_2m_max"][i],
            "min_temp": daglig_vader["temperature_2m_min"][i],
            "nederbord": daglig_vader["precipitation_sum"][i],
        }

        # Lägger till dagen i listan
        dagar.append(dag)

    return dagar
