from unittest.mock import Mock, patch

import pytest
import requests

from weather_api import hamta_vader, skapa_vaderlista

# =======================================
# Rensar cache före och efter varje test
# =======================================


@pytest.fixture(autouse=True)
def clear_cache():
    hamta_vader.cache_clear()
    yield
    hamta_vader.cache_clear()


# ====================================
# 2. Testar hämtning av väder från API
# ====================================


# Byter ut API anroper mot ett test
@patch("weather_api.requests.get")
def test_hamta_vader(mock_get):
    mock_get.return_value = Mock(
        json=lambda: {
            "current": {
                "temperature_2m": 8.1,
                "wind_speed_10m": 15.5,
            }
        }
    )
    # Hämtar väder med testdata
    data = hamta_vader(59.33, 18.07)

    # Kontrollera om temperature är rätt
    assert data["current"]["temperature_2m"] == 8.1


# ==================================
# 3. Testar fel vid timeout
# ==================================


@patch("weather_api.requests.get", side_effect=requests.Timeout)
def test_timeout(mock_get):
    with pytest.raises(RuntimeError):
        hamta_vader(59.33, 18.07)


# ====================================================================================
# Testar skapar ett vaderlista funktionen utan internet genom att använda exempeldata.
# ====================================================================================


def test_skapa_vaderlista():
    data = {
        "daily": {
            "time": ["2026-11-06", "2026-11-07", "2026-11-08"],
            "temperature_2m_max": [8.6, 8.4, 7.8],
            "temperature_2m_min": [3.2, 2.9, 2.5],
            "precipitation_sum": [0.0, 1.2, 0.5],
        }
    }

    dagar = skapa_vaderlista(data)

    assert len(dagar) == 3
    assert dagar[0]["max_temp"] == 8.6


# ======================================================
# Testar olika temperaturer: körs samma test tre gånger:
# ======================================================


@pytest.mark.parametrize(
    "max_temp, min_temp",
    [
        (8.6, 3.2),
        (15.0, 7.0),
        (-2.0, -8.0),
    ],
)
def test_skapa_vaderlista_temperaturer(max_temp, min_temp):
    data = {
        "daily": {
            "time": ["2026-11-07"],
            "temperature_2m_max": [max_temp],
            "temperature_2m_min": [min_temp],
            "precipitation_sum": [0.0],
        }
    }

    dagar = skapa_vaderlista(data)

    assert dagar[0]["max_temp"] == max_temp
    assert dagar[0]["min_temp"] == min_temp
