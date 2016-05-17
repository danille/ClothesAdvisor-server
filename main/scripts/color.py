class Color:
    def __init__(self, name, hue, saturation, value):
        self.name = name
        self.hue = hue
        self.saturation = saturation
        self.value = value

    def __str__(self):
        return 'Hue: {0}, Saturation: {1}, Value: {2}'.format(self.hue, self.saturation, self.value)

    def get_name(self):
        return self.name
