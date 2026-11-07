### Om projektet

En webbapplikation som visar väderprognoser för fem svenska städer. Applikationen hämtar väderinformation från Open-Meteo API och presenterar informationen på ett enkelt och tydligt sätt.

## Funktioner
- Välja mellan fem svenska städer.
- Visa aktuell temperatur och vindhastighet.
- Visa väderprognos för tre dagar.
- Visa högsta och lägsta temperatur samt nederbörd.
- Hantera fel om staden inte finns eller om API inte fungerar.

## Tekniker
- Python 3.10+
- Flask
- Requests
- Plotly
- Jinja2
- Pytest
- Ruff
- Bootstrap
- Open-Mateo API

### Installation

## 1. Ladda ner projektet

Klona repository:

```bash
git clone https://github.com/WardahSuhail/weather-app.git
cd weather-app
```

Alternativt kan du ladda ner projektet som ZIP via GitHubs **Code → Download ZIP** och extrahera filerna.

### 2. Skapa en virtuell miljö

**Windows:**
```bash
py -3 -m venv .venv
```

**macOS / Linux:**
```bash
python3 -m venv .venv
```

### 3. Aktivera miljön

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 4. Installera beroenden

Kör följande kommandon i projektets rotmapp:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements.dev.txt
```

### 5. Starta applikationen

```bash
flask run
```

Öppna sedan http://127.0.0.1:5000 i webbläsaren.

För att avsluta applikationen, tryck `Ctrl + C` i terminalen.

Avsluta den virtuella miljön med:

```bash
deactivate
```

## Köra tester

Aktivera den virtuella miljön och kör:

```bash
pytest
```

Pytest hittar och kör automatiskt projektets tester.

- **PASSED:** Testet har godkänts.
- **FAILED:** Testet har misslyckats. Pytest visar information om felet.

Du behöver inte starta Flask-applikationen separat för att köra testerna, förutsatt att testerna använder Flask:s testklient.

## Köra Ruff

Kontrollera kodden med:

```bash
ruff check .
```

Kontrollera formattering med:

```bash
ruff format --check .
```

## API och datakällor

Projektet använder [open-meteo.com API](https://open-meteo.com/en/docs?timezone=auto&current=temperature_2m,wind_speed_10m&hourly=&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&forecast_days=3) för att hämta aktuell väderinformation och väderprognoser.

Open-Meteo ger väderinformation för de valda städerna.

### Frågor och svar

- 1. Varför mockar du anropen mot API i dina tester, och vad skulle hända om du inte gjorde det?

- Jag mockar API anropen för att tersterna inte ska behöva hämta riktig information från internet. Istället använder jag testdata för att kontrollera att min kod fungerar. I tests/test_api.py använder jag @patch för att använda min test istället för riktiga API anrop.

- Exempel från tests/test_api.py:

```python
@patch("weather_api.requests.get")
def test_hamta_vader(mock_get):
    mock_get.return_value = Mock(json=lambda: DATA)
    resultat = hamta_vader(59.33, 18.07)
    assert resultat == DATA
```
- Om jag inte mockade anropen, skulle testerna behöva internet och API för att fungera. Och om ibland API inte fungerade kunde testerna också misslyckas.

- 2. Vad gör timeout och raise_for_status(), och varför behövs de?

- Jag använder timeout=5 i funktionen hamta_vader() i weather_api.py för att programmet inte ska vänta för länge på svar från API. raise_for_status() kontrollerar om API-anropet har fått ett HTTP-fel. Jag hanterar också fel från API och visar ett felmeddelande i appen i stället för att den kraschar.

- Exempel från weather_api.py:

```python
svar = requests.get(url_for, params=parametrar, timeout=5)
svar.raise_for_status()
return svar.json()
```

- 3. Hur fungerar mallarv i Jinja2? Förklara med exempel från dina egna mallar.

- Mallarv betyder att flera sidor kan använda samma grundmall. I mitt projekt är base.html grundmallen. index.html och vader.html använder den med extends och lägger in sitt eget innehåll i blocket content. På så sätt behöver jag inte skriva samma HTML-kod på varje sida.

- Exempel från base.html:

```html
{% block content %}
{% endblock %}
```
Exempel från index.html:

```html
{% extends "base.html" %}
{% block content %}
<h1>Weather App</h1>
{% endblock %}
```

- 4. Vad är en fixture, och vilken använder du?

- En fixture är en funktion som förbereder något som behövs när man kör tester. I mina tester använder jag en fixture som heter clear_cache. Den rensar cachen före och efter varje test så att gamla väderdata inte påverkar testresultaten.

Exempel från mina testfil:

```python
@pytest.fixture(autouse=True)
def clear_cache():
    hamta_vader.cache_clear()
    yield
    hamta_vader.cache_clear()
```

### Källor och referencer

Följande källor har använts under utvecklingen av projektet:

- [Open-Meteo API](https://open-meteo.com/): för att hämta väderinformation.
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs): för information om API-parametrar.
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/): för webbplatsens design och styling.
- [Bootstrap Cheatsheet](https://bootstrap-cheatsheet.themeselection.com/): som hjälp vid användning av Bootstrap.
- [Git-kommandon (PDF)](docs/git-kommandon.pdf): kursmaterial för Git-kommandon.


## Tack för du använder vår app!