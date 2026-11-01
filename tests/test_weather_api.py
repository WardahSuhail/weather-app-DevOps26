from unittest.mock import Mock, patch

import pytest
import requests

from weather_api import hamta_vader


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


# Tester timeout
@patch("weather_api.requests.get", side_effect=requests.Timeout)
def test_timeout(mock_get):
    with pytest.raises(RuntimeError):
        hamta_vader(59.33, 18.07)
