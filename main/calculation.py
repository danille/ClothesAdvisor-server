def calculate(fav_color, dis_color, weather, gender):
    filters = {'gender', 'season'}
    male_spring_clothes = {'hat', 'shirt', 'jacket', 'trousers', 'boots'}
    male_summer_clothes = {'hat', 'sunglasses', 'shirt', 'trousers', 'boots'}
    male_autumn_clothes = {'hat', 'scarf', 'shirt', 'sweater', 'jacket', 'trousers', 'boots'}
    male_winter_clothes = {'hat', 'scarf', 'shirt', 'sweater', 'jacket', 'trousers', 'boots'}
    female_spring_clothes = {'hat', 'shirt', 'jacket', 'skirt ', 'boots'}
    female_summer_clothes = {'hat', 'sunglasses', 'shirt', 'skirt', 'sandals'}
    female_autumn_clothes = {'hat', 'scarf', 'shirt', 'sweater', 'jacket', 'trousers', 'boots'}
    female_winter_clothes = {'hat', 'scarf', 'shirt', 'sweater', 'jacket', 'trousers', 'boots'}
    temp, weather_id = weather
    сolors_combinations = {'black': ['purple', 'white', 'red'],
                           'brown': ['blue', 'gold', 'beige'],
                           'beige': ['olive', 'turquoise', 'petrol'],
                           'gray': ['red', 'black', 'purple'],
                           'white': ['gold', 'silver', 'black'],
                           'blue': ['beige', 'silver', 'brown'],
                           'petrol': ['red', 'pink', 'beige'],
                           'turquoise': ['white', 'pink', 'gold'],
                           'green': ['red', 'white', 'yellow'],
                           'olive': ['beige', 'yellow', 'gold'],
                           'yellow': ['black', 'white', 'gray'],
                           'orange': ['green', 'brown', 'olive'],
                           'red': ['gray', 'white', 'beige'],
                           'pink': ['gray', 'black', 'white'],
                           'purple': ['white', 'silver', 'gold'],
                           'gold': ['white', 'beige', 'purple'],
                           }
    # Configure gender filter
    if gender == 0:
        filters['gender'] = 'female'
    elif gender == 1:
        filters['gender'] = 'male'

    # Configure season filter
    if temp < 0:
        filters['season'] = 'winter'
    elif 0 <= temp < 20 and weather_id in range(200, 622):
        filters['season'] = 'autumn'
    elif 0 <= temp < 20 and (weather_id == 500 or weather_id in range(700, 804)):
        filters['season'] = 'spring'
    elif temp >= 20:
        filters['season'] = 'summer'

    # Configure list of clothes
    if filters['gender'] == 'male' and filters['season'] == 'winter':
        clothes = male_winter_clothes
    elif filters['gender'] == 'male' and filters['season'] == 'spring':
        clothes = male_spring_clothes
    elif filters['gender'] == 'male' and filters['season'] == 'summer':
        clothes = male_summer_clothes
    elif filters['gender'] == 'male' and filters['season'] == 'autumn':
        clothes = male_autumn_clothes
