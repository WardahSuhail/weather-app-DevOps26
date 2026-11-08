# ===============================================
# En dictionary för städer med deras koordinater
# ===============================================
stader = {
    "Stockholm": {"latitud": 59.33, "longitud": 18.07},
    "Göteborg": {"latitud": 57.71, "longitud": 11.97},
    "Malmö": {"latitud": 55.61, "longitud": 13.00},
    "Umeå": {"latitud": 63.83, "longitud": 20.26},
    "Kiruna": {"latitud": 67.86, "longitud": 20.23},
}


# ======================================
# Kontrollerar om staden finns i listan
# ======================================
def kontrollera_stad(stad):
    return stad in stader
