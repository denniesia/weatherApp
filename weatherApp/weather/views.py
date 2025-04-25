from django.shortcuts import render
import datetime
import requests
from django.contrib import messages
from .helpers import  get_country, get_flag_url
# Create your views here.
def home(request):
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = 'Mülheim'
    url_cur = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=df7484304dfaba426eebf03161e567dd" #api weather cur

    PARAMS = {"units": "metric"} # preparing the data to be in that format


    try:
        data = requests.get(url_cur, params=PARAMS).json() # sends GET request to API, the result would be in json

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        longitude = data["coord"]["lon"]
        latitude = data["coord"]["lat"]

        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        country = get_country(str(latitude), str(longitude))
        flag_url = get_flag_url(country)

        day = datetime.date.today()

        context = {
            "city": city,
            "country": country,
            "description": description,
            "icon": icon,
            "temp": temp,
            "feels_like": feels_like,
            "humidity": humidity,
            "day": day,
            "flag_url": flag_url,
            'exception_occurred': False,
        }
        return render(request, 'index.html', context)
    except KeyError:
        context = {
            'exception_occurred': True,
        }

    return render(request, 'index.html', context)