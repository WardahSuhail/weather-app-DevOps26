import requests

# Adressen till väder-API
url = "https://api.open-meteo.com/v1/forecast"


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
        svar = requests.get(url, params=parametrar, timeout=5)

        # Kontrollerar om API-anropet gick bra
        svar.raise_for_status()

        # Gör om svaret till Python-data
        return svar.json()

    except requests.RequestException:
        # Visar ett felmeddelande om hämtningen misslyckas
        raise RuntimeError("Kunde inte hämta väderinformationen")
