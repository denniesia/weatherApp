import requests
from geopy import Nominatim

def get_location(lon,lat):

    geolocator = Nominatim(user_agent="weatherApp") #initializing geolocator, user_agent required for the OpenStreetMap 'identification policy'

    try:
        location = geolocator.reverse((lat,lon), exactly_one=True) #only one result, not a list
        if location and 'county' in location.raw['address']:
            country = location.raw['address']['country']
    except KeyError:
        country = "Unknown location"

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
        return f"https://flagcdn.com/w320/{country_code.lower()}.png"
    else:
            return None

