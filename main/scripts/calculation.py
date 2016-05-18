import json
import random
from urllib import error
from  urllib import request as url_req

from .Advice import Advice
from .Cloth import Cloth
from .Weather import Weather

male_spring_clothes_categories = ('mens-clothing-shirts', 'mens-clothing-jackets', 'mens-clothing-trousers-chinos')
male_summer_clothes_categories = ('mens-clothing-shirts', 'mens-clothing-trousers-chinos')
male_autumn_clothes_categories = (
    'mens-clothing-shirts', 'mens-clothing-jumpers-knitted-jumpers', 'mens-clothing-trousers-chinos')
male_winter_clothes_categories = (
    'mens-clothing-shirts', 'mens-clothing-jumpers-knitted-jumpers', 'mens-clothing-jackets', 'mens-clothing-jeans',)
female_spring_clothes_categories = (
    'womens-clothing-blouses-tunics', 'womens-clothing-jackets', 'womens-clothing-jeans')
female_summer_clothes_categories = ('womens-clothing-blouses-tunics', 'womens-clothing-skirts')
female_autumn_clothes_categories = (
    'bags-accessories-womens-scarves-shawls', 'womens-clothing-blouses-tunics', 'womens-clothing-jumpers-cardigans',
    'womens-clothing-coats', 'womens-clothing-trousers-leggings')
female_winter_clothes_categories = (
    'bags-accessories-womens-scarves-shawls', 'womens-clothing-blouses-tunics', 'womens-clothing-jumpers-cardigans',
    'womens-clothing-coats', 'womens-clothing-trousers-leggings')

colors_combinations = {'black': [['red', 'gray'], ['petrol', 'white']],
                       'brown': [['gray', 'olive'], ['yellow', 'beige']],
                       'beige': [['green', 'white'], ['orange', 'black']],
                       'gray': [['beige', 'white'], ['petrol', 'white']],
                       'white': [['olive', 'yellow'], ['orange', 'green']],
                       'blue': [['yellow', 'black'], ['gray', 'white']],
                       'petrol': [['turquoise', 'black'], ['pink', 'olive']],
                       'turquoise': [['gray', 'white'], ['petrol', 'yellow']],
                       'green': [['olive', 'yellow'], ['black', 'white']],
                       'olive': [['beige', 'white'], ['black', 'orange']],
                       'yellow': [['blue', 'white'], ['orange', 'black']],
                       'orange': [['olive', 'black'], ['blue', 'purple']],
                       'red': [['gray', 'orange'], ['black', 'beige']],
                       'pink': [['purple', 'white'], ['petrol', 'turquoise']],
                       'purple': [['brown', 'beige'], ['yellow', 'gray']],
                       }
color_distance = {'red': {'red': 0.0, 'brown': 48.729457210192685, 'blue': 207.0, 'beige': 85.08466371796976,
                          'gray': 105.5257788410017, 'purple': 282.55811791558915, 'pink': 0.0,
                          'black': 141.4213562373095, 'orange': 35.431765409022454, 'petrol': 193.85203119905657,
                          'turquoise': 196.65411259366024, 'olive': 74.6629760992689, 'green': 130.4153365214383,
                          'yellow': 52.18361811909941, 'white': 100.0},
                  'brown': {'red': 48.729457210192685, 'brown': 0.0, 'blue': 181.11753090189805,
                            'beige': 83.29729887577388, 'gray': 104.50880345693372, 'purple': 249.07968604444642,
                            'pink': 48.729457210192685, 'black': 121.22112027200541, 'orange': 25.675864152935528,
                            'petrol': 159.0694502410818, 'turquoise': 171.4858594753515, 'olive': 32.159601987586846,
                            'green': 94.02127418834527, 'yellow': 40.588791556290516, 'white': 111.2409996359256},
                  'blue': {'red': 207.0, 'brown': 181.11753090189805, 'blue': 0.0, 'beige': 194.08348719043565,
                           'gray': 232.34605656218915, 'purple': 84.74721234353376, 'pink': 207.0,
                           'black': 250.69702830308938, 'orange': 174.4775343704742, 'petrol': 46.707708143303286,
                           'turquoise': 34.72520698282445, 'olive': 150.8494613845207, 'green': 92.31012945500618,
                           'yellow': 155.0616973981647, 'white': 229.88910370002316},
                  'beige': {'red': 85.08466371796976, 'brown': 83.29729887577388, 'blue': 194.08348719043565,
                            'beige': 0.0, 'gray': 42.973596544855305, 'purple': 263.2856433609702,
                            'pink': 85.08466371796976, 'black': 95.9135026990465, 'orange': 78.87135094570144,
                            'petrol': 180.26461105829952, 'turquoise': 170.87281820114046, 'olive': 90.25231298975112,
                            'green': 126.04142176284746, 'yellow': 81.35361086024393, 'white': 38.462969204157915},
                  'gray': {'red': 105.5257788410017, 'brown': 104.50880345693372, 'blue': 232.34605656218915,
                           'beige': 42.973596544855305, 'gray': 0.0, 'purple': 296.58388358101996,
                           'pink': 105.5257788410017, 'black': 66.3, 'orange': 107.33890254702625,
                           'petrol': 214.03121267702988, 'turquoise': 208.25112244595465, 'olive': 117.92544254739941,
                           'green': 159.4392987942433, 'yellow': 115.7972365818805, 'white': 33.7},
                  'purple': {'red': 282.55811791558915, 'brown': 249.07968604444642, 'blue': 84.74721234353376,
                             'beige': 263.2856433609702, 'gray': 296.58388358101996, 'purple': 0.0,
                             'pink': 282.55811791558915, 'black': 301.4947594901112, 'orange': 248.04685041338462,
                             'petrol': 90.01422109866863, 'turquoise': 101.29131255937007, 'olive': 217.0221417275205,
                             'green': 155.05963368975176, 'yellow': 230.56842802083725, 'white': 299.73169668888875},
                  'pink': {'red': 0.0, 'brown': 48.729457210192685, 'blue': 207.0, 'beige': 85.08466371796976,
                           'gray': 105.5257788410017, 'purple': 282.55811791558915, 'pink': 0.0,
                           'black': 141.4213562373095, 'orange': 35.431765409022454, 'petrol': 193.85203119905657,
                           'turquoise': 196.65411259366024, 'olive': 74.6629760992689, 'green': 130.4153365214383,
                           'yellow': 52.18361811909941, 'white': 100.0},
                  'black': {'red': 141.4213562373095, 'brown': 121.22112027200541, 'blue': 250.69702830308938,
                            'beige': 95.9135026990465, 'gray': 66.3, 'purple': 301.4947594901112,
                            'pink': 141.4213562373095, 'black': 0.0, 'orange': 136.65800379048423,
                            'petrol': 221.26592598048168, 'turquoise': 228.5450502636187, 'olive': 131.35661384186182,
                            'green': 170.0828033635382, 'yellow': 147.31982215574388, 'white': 100.0},
                  'orange': {'red': 35.431765409022454, 'brown': 25.675864152935528, 'blue': 174.4775343704742,
                             'beige': 78.87135094570144, 'gray': 107.33890254702625, 'purple': 248.04685041338462,
                             'pink': 35.431765409022454, 'black': 136.65800379048423, 'orange': 0.0,
                             'petrol': 158.89631839661988, 'turquoise': 164.69441399148909, 'olive': 40.80061274049692,
                             'green': 95.06445182085677, 'yellow': 20.871032557111306, 'white': 106.09151709726844},
                  'petrol': {'red': 193.85203119905657, 'brown': 159.0694502410818, 'blue': 46.707708143303286,
                             'beige': 180.26461105829952, 'gray': 214.03121267702988, 'purple': 90.01422109866863,
                             'pink': 193.85203119905657, 'black': 221.26592598048168, 'orange': 158.89631839661988,
                             'petrol': 0.0, 'turquoise': 54.03193500144151, 'olive': 127.00885795880538,
                             'green': 65.05605275452854, 'yellow': 142.3905895766992, 'white': 218.12521633227095},
                  'turquoise': {'red': 196.65411259366024, 'brown': 171.4858594753515, 'blue': 34.72520698282445,
                                'beige': 170.87281820114046, 'gray': 208.25112244595465, 'purple': 101.29131255937007,
                                'pink': 196.65411259366024, 'black': 228.5450502636187, 'orange': 164.69441399148909,
                                'petrol': 54.03193500144151, 'turquoise': 0.0, 'olive': 142.09644612023203,
                                'green': 87.0, 'yellow': 145.49381430150217, 'white': 205.5063016065444},
                  'olive': {'red': 74.6629760992689, 'brown': 32.159601987586846, 'blue': 150.8494613845207,
                            'beige': 90.25231298975112, 'gray': 117.92544254739941, 'purple': 217.0221417275205,
                            'pink': 74.6629760992689, 'black': 131.35661384186182, 'orange': 40.80061274049692,
                            'petrol': 127.00885795880538, 'turquoise': 142.09644612023203, 'olive': 0.0,
                            'green': 62.01161181585268, 'yellow': 38.62550970537477, 'white': 124.79807690826009},
                  'green': {'red': 130.4153365214383, 'brown': 94.02127418834527, 'blue': 92.31012945500618,
                            'beige': 126.04142176284746, 'gray': 159.4392987942433, 'purple': 155.05963368975176,
                            'pink': 130.4153365214383, 'black': 170.0828033635382, 'orange': 95.06445182085677,
                            'petrol': 65.05605275452854, 'turquoise': 87.0, 'olive': 62.01161181585268, 'green': 0.0,
                            'yellow': 80.547191136625, 'white': 164.34159546505566},
                  'yellow': {'red': 52.18361811909941, 'brown': 40.588791556290516, 'blue': 155.0616973981647,
                             'beige': 81.35361086024393, 'gray': 115.7972365818805, 'purple': 230.56842802083725,
                             'pink': 52.18361811909941, 'black': 147.31982215574388, 'orange': 20.871032557111306,
                             'petrol': 142.3905895766992, 'turquoise': 145.49381430150217, 'olive': 38.62550970537477,
                             'green': 80.547191136625, 'yellow': 0.0, 'white': 112.08536925040663},
                  'white': {'red': 100.0, 'brown': 111.2409996359256, 'blue': 229.88910370002316,
                            'beige': 38.462969204157915, 'gray': 33.7, 'purple': 299.73169668888875, 'pink': 100.0,
                            'black': 100.0, 'orange': 106.09151709726844, 'petrol': 218.12521633227095,
                            'turquoise': 205.5063016065444, 'olive': 124.79807690826009, 'green': 164.34159546505566,
                            'yellow': 112.08536925040663, 'white': 0.0}}


# Calculating
def calculate(fav_color, dis_color, weather, gender):
    advice = Advice()
    __weather__ = Weather(weather)
    advice.add_weather(__weather__)
    temp, weather_id = weather
    season = ''
    __gender__ = ''
    # Configure gender filter
    if gender == 0:
        __gender__ = 'womens'
    elif gender == 1:
        __gender__ = 'mens'

    # Configure season filter
    if temp < 0:
        __season__ = 'winter'
    elif 0 <= temp < 20 and weather_id in range(200, 622):
        __season__ = 'autumn'
    elif 0 <= temp < 20 and (weather_id == 500 or weather_id in range(700, 804)):
        __season__ = 'spring'
    elif temp >= 20:
        __season__ = 'summer'

    def define_set_of_colors_for_clothes():
        def get_distance_between_colors(color1, color2):
            return color_distance[color1][color2]

        set_of_colors_for_clothes = [fav_color]
        colors_sets = colors_combinations[fav_color]
        set1 = colors_sets[0]
        set2 = colors_sets[1]
        if min(get_distance_between_colors(set1[0], dis_color), get_distance_between_colors(set1[1], dis_color)) > min(
                get_distance_between_colors(set2[0], dis_color), get_distance_between_colors(set2[1], dis_color)):
            for color in set1:
                set_of_colors_for_clothes.append(color)
        else:
            for color in set2:
                set_of_colors_for_clothes.append(color)
        return set_of_colors_for_clothes

    def make_zalando_request(url):
        requested_bytes_from_zalando = url_req.urlopen(url).read()
        json_string = str(requested_bytes_from_zalando, encoding='utf-8')
        received_clothes = json.loads(json_string)['content']
        received_cloth = received_clothes[random.randint(0, len(received_clothes) - 1)]
        cloth_name = received_cloth['name']
        cloth_shop_url = received_cloth['shopUrl']
        cloth_available = received_cloth['available']
        cloth_brand_logo = received_cloth['brand']['logoLargeUrl']
        cloth_price = received_cloth['units'][0]['price']['formatted']
        cloth_img = received_cloth['media']['images'][2]['smallHdUrl']
        advice.add_cloth(Cloth(cloth_name, cloth_shop_url, cloth_available, cloth_brand_logo, cloth_price, cloth_img))
        print('OK!')

    __colors__ = define_set_of_colors_for_clothes()

    def configure_advice_for_categories(categories, season):
        for clothes_category in categories:
            index = int(random.random() * len(__colors__) - 1)
            color = __colors__[index]
            url_for_request = 'https://api.zalando.com/articles?category={0}&season={1}&color={2}'.format(
                clothes_category, season, color)
            try:
                make_zalando_request(url_for_request)
            except error.HTTPError:
                advice.add_message('{0} {1}'.format(color, clothes_category))

    if __gender__ == 'womens':
        if __season__ == 'winter':
            configure_advice_for_categories(female_winter_clothes_categories, 'winter')

        if __season__ == 'spring':
            configure_advice_for_categories(female_spring_clothes_categories, 'summer')

        if __season__ == 'summer':
            configure_advice_for_categories(female_summer_clothes_categories, 'summer')

        if __season__ == 'autumn':
            configure_advice_for_categories(female_autumn_clothes_categories, 'winter')

    elif __gender__ == 'mens':
        if __season__ == 'winter':
            configure_advice_for_categories(male_winter_clothes_categories, 'winter')

        if __season__ == 'spring':
            configure_advice_for_categories(male_spring_clothes_categories, 'summer')

        if __season__ == 'summer':
            configure_advice_for_categories(male_summer_clothes_categories, 'summer')

        if __season__ == 'autumn':
            configure_advice_for_categories(male_autumn_clothes_categories, 'winter')

    return advice
