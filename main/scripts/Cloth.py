class Cloth:
    def __init__(self, name, shop_url, available, brand_logo, price, img_url):
        self.name = name
        self.shop_url = shop_url
        self.available = available
        self.brand_logo = brand_logo
        self.price = price
        self.img_url = img_url

    def __str__(self):
        print('Name: {0}\nBrand: {1}\nPrice: {2}\nAvailable: {3}, Link to the shop: {4}'.format(self.name, self.brand,
                                                                                                self.price,
                                                                                                self.available,
                                                                                                self.shop_url))
