import json
import random
from urllib import error
from urllib import request as url_req

from .Advice import Advice
from .Cloth import Cloth
from .Weather import Weather

male_spring_clothes_categories = ('mens-clothing-t-shirts', 'mens-clothing-jumpers-cardigans', 'mens-clothing-jeans')
male_summer_clothes_categories = ('mens-clothing-t-shirts', 'mens-clothing-shorts', 'mens-sunglasses')
male_autumn_clothes_categories = (
    'mens-clothing-shirts', 'mens-clothing-jumpers-cardigans', 'mens-clothing-jeans')
male_winter_clothes_categories = (
    'mens-clothing-jumpers-knitted-jumpers', 'mens-clothing-jackets', 'mens-clothing-jeans',)
female_spring_clothes_categories = (
    'womens-clothing-blouses-tunics', 'womens-clothing-jackets', 'womens-clothing-jeans')
female_summer_clothes_categories = ('womens-clothing-blouses-tunics', 'womens-clothing-skirts')
female_autumn_clothes_categories = (
    'womens-clothing-jumpers-cardigans',
    'womens-clothing-coats',
    'womens-clothing-trousers-leggings')
female_winter_clothes_categories = (
    'bags-accessories-womens-scarves-shawls', 'womens-clothing-blouses-tunics', 'womens-clothing-jumpers-cardigans',
    'womens-clothing-coats', 'womens-clothing-trousers-leggings')

colors_combinations = [('black', 'red', 'gray'), ('black', 'petrol', 'white'),
                       ('brown', 'gray', 'olive'), ('brown', 'yellow', 'beige'),
                       ('beige', 'green', 'white'), ('beige', 'orange', 'black'),
                       ('gray', 'beige', 'white'), ('gray', 'petrol', 'white'),
                       ('white', 'olive', 'yellow'), ('white', 'orange', 'green'),
                       ('blue', 'yellow', 'black'), ('blue', 'gray', 'white'),
                       ('petrol', 'turquoise', 'black'), ('petrol', 'pink', 'olive'),
                       ('turquoise', 'gray', 'white'), ('turquoise', 'petrol', 'yellow'),
                       ('green', 'olive', 'yellow'), ('green', 'black', 'white'),
                       ('olive', 'beige', 'white'), ('olive', 'black', 'orange'),
                       ('yellow', 'blue', 'white'), ('yellow', 'orange', 'black'),
                       ('orange', 'olive', 'black'), ('orange', 'blue', 'purple'),
                       ('red', 'gray', 'orange'), ('red', 'black', 'beige'),
                       ('pink', 'purple', 'white'), ('pink', 'petrol', 'turquoise'),
                       ('purple', 'brown', 'beige'), ('purple', 'yellow', 'gray')]


# Perform calculations and configure advice. Ready for response
def calculate(fav_colors, unfav_color, weather, gender):
    advice = Advice()
    __weather__ = Weather(weather)
    advice.add_weather(__weather__)
    temp, weather_id = weather
    __season__ = ''
    __gender__ = ''

    # Define colors using Sorensen similarity index
    def define_set_of_colors_for_clothes():
        def get_sorensen_index(colors1, colors2):
            return len(set(colors1).intersection(colors2)) / (len(colors1) + len(colors2))

        max_index = -1
        set_to_return = ()

        for colors_set in colors_combinations:
            index_of_similarity = get_sorensen_index(colors_set, fav_colors)

            # # Check if non-favourite color is in current colors set
            # If it is, then decrease index of similarity in 2 times
            if unfav_color in colors_set:
                index_of_similarity *= 0.5
            if index_of_similarity > max_index:
                max_index = index_of_similarity
                set_to_return = colors_set
        return set_to_return

    __colors__ = define_set_of_colors_for_clothes()

    def configure_advice_for_categories(categories, season):
        # Make request to Zalando API, parse response and add clothes item to the Advice
        def make_zalando_request(url):
            requested_bytes_from_zalando = url_req.urlopen(url).read()
            json_string = str(requested_bytes_from_zalando, encoding='utf-8')
            received_clothes = json.loads(json_string)['content']
            while len(received_clothes) == 0:  # sh*t, but works
                continue
            received_cloth = received_clothes[random.randint(0, len(received_clothes) - 1)]
            print(received_cloth)
            cloth_name = received_cloth['name']
            cloth_shop_url = received_cloth['shopUrl']
            cloth_available = received_cloth['available']
            try:
                cloth_brand_logo = received_cloth['brand']['logoLargeUrl']
            except KeyError:
                cloth_brand_logo = 'http://mih.com.au/wp-content/uploads/2014/07/brand.png'  # 'http://s32.postimg.org/67euw00xx/brand_logo.jpg'
            cloth_price = received_cloth['units'][0]['price']['formatted']
            cloth_img = received_cloth['media']['images'][2]['smallHdUrl']
            advice.add_cloth(
                Cloth(cloth_name, cloth_shop_url, cloth_available, cloth_brand_logo, cloth_price, cloth_img))

        for clothes_category in categories:
            index = int(random.random() * len(__colors__) - 1)
            color = __colors__[index]
            url_for_request = 'https://api.zalando.com/articles?category={0}&season={1}&color={2}'.format(
                clothes_category, season, color)
            try:
                make_zalando_request(url_for_request)
            except error.HTTPError:
                advice.add_message('{0} {1}'.format(color, clothes_category))

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
