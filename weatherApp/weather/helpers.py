import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

def get_country(lat, lon):
    geolocator = Nominatim(user_agent="weatherApp", timeout=10)  # increase timeout to 10 seconds

    location = geolocator.reverse((lat, lon), exactly_one=True, language="en")

    if location:
        return location.raw['address']['country']
    else:
        return "Unknown country"



def get_country_code(country_name):
    url = f'https://restcountries.com/v3.1/name/{country_name}?fullText=true'
    try:
        data_response = requests.get(url).json()
        country_code = data_response[0]['cca2'] # 'cca2' is the 2-letter country code
        return country_code
    except KeyError:
        country_code = "Unknown country"

def get_flag_url(country_name):
    country_code = get_country_code(country_name)

    if country_code != "Unknown country":
        return f"https://flagcdn.com/w80/{country_code.lower()}.png"
    else:
        return None

