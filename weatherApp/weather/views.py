from django.shortcuts import render, HttpResponse
import datetime
import requests
# Create your views here.
def home(request):
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = 'Mülheim'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=df7484304dfaba426eebf03161e567dd"
    PARAMS = {"units": "metric"} # preparing the data to be in that format

    data = requests.get(url, params=PARAMS).json() # sends GET request to API, the result would be in json

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    context = {
        "description": description,
        "icon": icon,
        "temp": temp,
        "day": day,
    }

    return render(request, 'index.html', context)