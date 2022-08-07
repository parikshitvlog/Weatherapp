from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "longitude": str(json_data['coord']['lon']),
            "latitude": str(json_data['coord']['lat']),
         
            
            "temp": str(json_data['main']['temp'])+'k',
            
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'weatherapp/index.html', {'city': city, 'data': data})