from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request as url_req
import json


# Create your views here.
@api_view(['GET', 'POST'])
def get_advice(request):
    if request.method == 'POST':
        print('TEST')

        # Retrieving data from User: fetching URL-query parameters
        sex = request.query_params.get('s')  # User's sex
        req_lat = request.query_params.get('lat')  # User's current latitude
        req_lon = request.query_params.get('lon')  # User's current latitude
        fav_color = request.query_params.get('f_col')  # User's favourite color
        dis_color = request.query_params.get('d_col')  # User's unloved color
        day_index = int(request.query_params.get('d_ind'))  # Day required by User : 0 - today, 8 - week later

        # Retrieving weather forecast from OpenWeatherMap API for required day and
        get_weather(req_lat, req_lon, day_index)
        return Response(data=None, status=status.HTTP_200_OK)


def get_weather(lat, lon, day_index):
    app_key = '0c5c10c03eb74a75a2f4c1999d9ee376'  # App key required for access OpenWeatherMap API
    # Formatted URL with query parameters
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?APPID=' + app_key + '&lat=' + lat + '&lon=' + lon + '&units=metric&cnt=8'
    requested_url_bytes = url_req.urlopen(url).read()  # Bytes literals which contain JSON-response
    json_string = str(requested_url_bytes, encoding='utf-8')  # Convert bytes literals to string
    weather = json.loads(json_string)  # Parsing string to JSON
    if weather['cod'] == '404':
        print('Error occurred')
    else:
        average_daily_temp = weather['list'][day_index]['temp']['day']  # Average temperature in required day
        weather_conditions = weather['list'][day_index]['weather'][0]['id']  # Rain params in required day
        print(average_daily_temp)
        print(weather_conditions)
        return average_daily_temp, weather_conditions


