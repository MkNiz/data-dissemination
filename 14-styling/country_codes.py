from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Retrieves pygal's 2-digit country code for a country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Return None if none found
    return None
