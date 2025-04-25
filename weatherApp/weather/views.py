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
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=df7484304dfaba426eebf03161e567dd"
    PARAMS = {"units": "metric"} # preparing the data to be in that format


    try:
        data = requests.get(url, params=PARAMS).json() # sends GET request to API, the result would be in json

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        longitude = data["coord"]["lon"]
        latitude = data["coord"]["lat"]

        country = get_country(str(latitude), str(longitude))
        flag_url = get_flag_url(country)

        day = datetime.date.today()

        context = {
            "city": city,
            "country": country,
            "description": description,
            "icon": icon,
            "temp": temp,
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