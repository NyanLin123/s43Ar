class TP_env(object):

    prices = [322, 882, 2, 291, 882, 928, 201]
    max_price_addon = 20

    def __init__(self):
        self.time = 0
        self.stock = 20

    def do(self, action):

        return {'price': price, 'instock': self.stock}
