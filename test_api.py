import requests

# Adressen till väder-API
url = "https://api.open-meteo.com/v1/forecast"

# Väljer vilken väderinformation vi vill ha
parametrar = {
    "latitude": 59.33,
    "longitude": 18.07,
    "current": "temperature_2m,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto",
    "forecast_days": 3,
}

# Hämtar väderinformation från API
svar = requests.get(url, params=parametrar, timeout=5)

# Kontrollerar om API-anropet gick bra
svar.raise_for_status()

# Gör om svar till Pyton data
data = svar.json()

# Skriver ut svaret
print(data)
