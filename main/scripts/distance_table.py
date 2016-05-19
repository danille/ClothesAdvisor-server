from math import sqrt

from main.scripts.color import Color


def make_table():
    colors_distance = {
        'black': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'brown': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'beige': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'gray': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                 'petrol': 0, 'turquoise': 0, 'green': 0,
                 'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'white': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'blue': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                 'petrol': 0, 'turquoise': 0, 'green': 0,
                 'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'petrol': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                   'petrol': 0, 'turquoise': 0, 'green': 0,
                   'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'turquoise': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                      'petrol': 0, 'turquoise': 0, 'green': 0,
                      'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'green': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'olive': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                  'petrol': 0, 'turquoise': 0, 'green': 0,
                  'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'yellow': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                   'petrol': 0, 'turquoise': 0, 'green': 0,
                   'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'orange': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                   'petrol': 0, 'turquoise': 0, 'green': 0,
                   'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'red': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                'petrol': 0, 'turquoise': 0, 'green': 0,
                'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'pink': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                 'petrol': 0, 'turquoise': 0, 'green': 0,
                 'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
        'purple': {'black': 0, 'brown': 0, 'beige': 0, 'gray': 0, 'white': 0, 'blue': 0,
                   'petrol': 0, 'turquoise': 0, 'green': 0,
                   'olive': 0, 'yellow': 0, 'orange': 0, 'red': 0, 'pink': 0, 'purple': 0},
    }
    colors = [Color('black', 0, 0.0, 0.0),
              Color('brown', 30, 100.0, 61.6),
              Color('beige', 30, 21.2, 88.6),
              Color('gray', 0, 0.0, 66.3),
              Color('white', 0, 0.0, 100.0),
              Color('blue', 207, 100.0, 100.0),
              Color('petrol', 189, 100.0, 56.9),
              Color('turquoise', 194, 67.8, 100.0),
              Color('green', 124, 100.0, 59.6),
              Color('olive', 62, 100.0, 58.4),
              Color('yellow', 52, 99.2, 95.7),
              Color('orange', 33, 100.0, 87.1),
              Color('red', 0, 100.0, 100.0),
              Color('pink', 0, 100.0, 100.0),
              Color('purple', 279, 100.0, 55.3)]
    print(end='\t\t')
    for color in colors:
        print(color.name, end='\t')
    for color1 in colors:
        print('')
        print(color1.name, end='\t')
        for color2 in colors:
            distance = sqrt(((color1.hue - color2.hue) ** 2) + ((color1.saturation - color2.saturation) ** 2) + (
                (color1.value - color2.value) ** 2))
            colors_distance[color1.name][color2.name] = distance
            print('%.2f' % distance, end='\t')
        print('')
    return colors_distance


color_distance = make_table()
print(color_distance)
