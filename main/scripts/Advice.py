class Advice:
    def __init__(self):
        self.clothes = []
        self.weather = None

    def add_cloth(self, cloth):
        self.clothes.append(cloth)

    def add_message(self, message):
        self.clothes.append(message)

    def add_weather(self, weather):
        self.weather = weather
