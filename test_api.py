from unittest.mock import Mock, patch

import requests
import pytest

from weather_api import hamta_vader


# Rensar cache före och efter varje test
@pytest.fixture(autouse=True)
def clear_cache():
    hamta_vader.cache_clear()
    yield
    hamta_vader.cache_clear()


# Fejkad väderdata.
DATA = {
    "current": {
        "temperature_2m": 12.5,
        "wind_speed_10m": 8.0,
    },
    "daily": {
        "time": ["2026-11-07", "2026-11-08", "2026-11-09"],
        "temperature_2m_max": [13.0, 14.0, 12.0],
        "temperature_2m_min": [5.0, 6.0, 4.0],
        "precipitation_sum": [0.0, 2.5, 1.0],
    },
}


# Testar om väderinformationen hämtas rätt
@patch("weather_api.requests.get")
def test_hamta_vader(mock_get):
    mock_get.return_value = Mock(json=lambda: DATA)

    resultat = hamta_vader(59.33, 18.07)
    assert resultat == DATA


# Testar om timeout-fel fungerar
@patch("weather_api.requests.get")
def test_hamta_vader_timeout(mock_get):
    mock_get.side_effect = requests.Timeout

    with pytest.raises(RuntimeError):
        hamta_vader(59.33, 18.07)


# Testar om HTTP-fel fungerar
@patch("weather_api.requests.get")
def test_hamta_vader_http_error(mock_get):
    mock_get.return_value = Mock()
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError

    with pytest.raises(RuntimeError):
        hamta_vader(59.33, 18.07)
