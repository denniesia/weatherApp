from django.shortcuts import render
import datetime
import requests
from django.contrib import messages
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

        day = datetime.date.today()

        context = {
            "city": city,
            "description": description,
            "icon": icon,
            "temp": temp,
            "day": day,
            'exception_occurred': False,
        }
        return render(request, 'index.html', context)
    except KeyError:
        messages.error(request, 'Entered data is not available to API')
        context = {
            'exception_occurred': True,
        }

    return render(request, 'index.html', context)