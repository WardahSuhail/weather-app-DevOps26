# Hämtar funktionen hello från app.py
from app import app


# Tester startsidan.
def test_hello():
    klient = app.test_client()
    svar = klient.get("/")

    # Ser om sidan fungerar och visar rätt text.
    assert svar.status_code == 200
    assert b"Hello World!" in svar.data
