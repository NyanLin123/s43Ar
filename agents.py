class TP_env:

    prices = [322, 882, 2, 291, 882, 928, 201]
    max_price_addon = 20

    def __init__(self):
        self.time = 0
        self.stock = 20
        self.stock_history = []
        self.price_history = []

    def initial_percepts(self):
        # return initial percepts
        self.stock_history.append(self.stock)
        print(self.prices[0])

    def do():
        return 'hello'


class TP_agent(Agent):
    def __init__(self, env):
        self.env = env
        self.spent = 0
        precetps = env.initial_percetps()
        self.ave = self.last_price = precepts['price']
        self.instock = precetps['instock']

    def go(self, n):
        # go for n time steps
        for i in range(n):
            if self.last_price < 0.9*self.ave and self.instock < 60:
                tobuy = 48


print('hello')
