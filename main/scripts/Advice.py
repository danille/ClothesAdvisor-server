class Advice:
    def __init__(self):
        self.clothes = []
        self.temp = 0
        self.conditions = 0
        self.message = ''

    def add_cloth(self, cloth):
        self.clothes.append(cloth)

    def add_message(self, message):
        self.clothes.append(message)

    def add_weather(self, weather):
        self.temp = weather[0]
        self.conditions = weather[1]
