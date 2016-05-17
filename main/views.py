import json
import urllib.request as url_req

from django.http import JsonResponse

from .scripts.calculation import calculate


# Create your views here.
# @api_view(['GET', 'POST'])
# def get_advice(request):
#     key = request.query_params.get('key')
#     danil_key = 'danil_key'
#     if request.method == 'GET' and key != danil_key:
#
#         # Retrieving data from User: fetching URL-query parameters
#         sex = request.query_params.get('s')  # User's sex
#         req_lat = request.query_params.get('lat')  # User's current latitude
#         req_lon = request.query_params.get('lon')  # User's current latitude
#         fav_color = request.query_params.get('f_col')  # User's favourite color
#         dis_color = request.query_params.get('d_col')  # User's unloved color
#         day_index = int(request.query_params.get('d_ind'))  # Day required by User : 0 - today, 8 - week later
#         # Retrieving weather forecast from OpenWeatherMap API for required day and
#         weather = get_weather(req_lat, req_lon, day_index)
#         return Response({'sex': sex, 'weather': weather}, status=status.HTTP_200_OK)
#     else:
#         return Response({'key': 'value'}, status=status.HTTP_200_OK)
#
def get_advice(request):
    # key = request.GET.get('key')
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    fav_color = request.GET.get('f_col')
    unfav_color = request.GET.get('d_col')
    day_index = request.GET.get('d_ind')
    gender = int(request.GET.get('gnd'))
    day_index = int(day_index)

    if request.method == 'GET':
        weather = get_weather(lat, lon, day_index)
        calculate(fav_color, unfav_color, weather, gender)
        return JsonResponse({'temp': weather[0], 'cond': weather[1]})


def get_weather(lat, lon, day_index):
    app_key = '0c5c10c03eb74a75a2f4c1999d9ee376'  # App key required for access OpenWeatherMap API
    # Formatted URL with query parameters
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?APPID={0}&lat={1}&lon={2}&units=metric&cnt=8'.format(
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

#
# class AdviceViewSet(viewsets.ModelViewSet):
#     queryset = Advice.objects.all()
#     serializer_class = AdviceSerializer
