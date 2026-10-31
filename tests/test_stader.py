from app import kontrollera_stad

# Tester om en stad finn i listan
def test_kontrollera_stad():
    assert kontrollera_stad("Stockholm") is True
    assert kontrollera_stad("Göteborg") is True
    assert kontrollera_stad("Malmö") is True
    assert kontrollera_stad("Umeå") is True
    assert kontrollera_stad("Kiruna") is True
    assert kontrollera_stad("Dubai") is False
    assert kontrollera_stad("Karachi") is False