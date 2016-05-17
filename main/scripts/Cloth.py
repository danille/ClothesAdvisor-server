class Cloth:
    def __init__(self, season, gender):
        self.category = ''
        self.season = season
        self.gender = gender
        self.color = ''
        self.available = 0
        self.url = ''
        self.img_url = ''

    def set_category(self, category):
        self.category = category

    def set_color(self, color):
        self.color = color

    def set_url(self, url):
        self.url = url

    def set_img_url(self, img_url):
        self.img_url = img_url
