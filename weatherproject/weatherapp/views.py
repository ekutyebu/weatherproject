from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.

def home(request):

    """
    weather API call
    """
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=86cb0f95e8d89a3d8f40ffa6f0111037"
    PARAMS = {'units':'metric'}

    # API_KEY = '86cb0f95e8d89a3d8f40ffa6f0111037'
    # SEARCH_ENGINE_ID = '52ca4b20894a24997'
    # query = city + ' weather'
    # page = 1
    # start = (page - 1) * 10
    # searchType = 'image'
    # search_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"

    try:
        data = requests.get(url.format(city=city), params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()
        """
        Render the home page of the weather application.
        """
        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
        }
        return render(request, 'weatherapp/index.html', context)
    except Exception as e:
        print(e)
        context = {
            'description': 'City not found',
            'icon': '01d',
            'temp': 0,
            'day': datetime.date.today(),
            'city': 'Douala',
        }
        return render(request, 'weatherapp/index.html', context)

    
