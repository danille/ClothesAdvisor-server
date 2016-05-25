import json
import urllib.request as url_req

from django.http import JsonResponse

from .scripts.calculation import calculate


def get_advice(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    fav_colors = (request.GET.get('fo_col'), request.GET.get('ft_col'), request.GET.get('fth_col'))
    unfav_color = request.GET.get('d_col')
    day_index = request.GET.get('d_ind')
    gender = int(request.GET.get('gnd'))
    day_index = int(day_index)

    if request.method == 'GET':
        weather = get_weather(lat, lon, day_index)
        advice = calculate(fav_colors, unfav_color, weather, gender)
        json_string_advice = json.dumps(advice, default=lambda o: o.__dict__)
        advice_json = json.loads(json_string_advice)
        return JsonResponse(advice_json, safe=False)


def get_weather(lat, lon, day_index):
    app_key = '0c5c10c03eb74a75a2f4c1999d9ee376'  # App key required for access OpenWeatherMap API
    # Formatted URL with query parameters
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?APPID={0}&lat={1}&lon={2}&units=metric&cnt=16'.format(
        app_key, lat, lon)

    requested_url_bytes = url_req.urlopen(url).read()  # Bytes literals which contain JSON-response
    json_string = str(requested_url_bytes, encoding='utf-8')  # Convert bytes literals to string
    weather = json.loads(json_string)  # Parsing string to JSON
    if weather['cod'] == '404':
        print('Error occurred')
    else:
        average_daily_temp = float(weather['list'][day_index]['temp']['day'])  # Average temperature in required day
        weather_conditions = int(weather['list'][day_index]['weather'][0]['id'])  # Rain params in required day
        return average_daily_temp, weather_conditions
