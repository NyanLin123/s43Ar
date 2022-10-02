import random

class Agent(object):
    def __init__(self, env):
        """ set up the agent"""
        self.env = env

    def go(self, n):
        # acts for n time setps
        raise NotImplementedError("go")

class TP_agent(Agent):
    def __init__(self, env):
        self.env = env
        self.spent = 0
        percetps = env.initial_percepts()
        self.ave = self.last_price = percetps['price']
        self.instock = percetps['instock']

    def go(self, n):
        """go for n time steps"""
        for i in range(n):
            if self.last_price < 0.9*self.ave:
                tobuy = 48
            elif self.instock < 12:
                tobuy = 12
            else:
                tobuy = 0
            
            self.spent += tobuy*self.last_price
        return self.instock



class TP_env:
    prices = [232,122,92,432,22]
    max_price_adon = 20 #maximum of random value added to get prices

    def __init__(self):
        self.time = 0
        self.stock = 20
        self.stock_history = []
        self.price_history = []

    def initial_percepts(self):
        self.stock_history.append(self.stock)
        price = self.prices[0]+random.randrange(self.max_price_adon)
        self.price_history.append(price)
        return {'price':price, 'instock': self.stock}

    def do(self, action):
        used = pick_from_dist({6:0.11,5:0.1,4:3.2})
        return self.max_price_adon

    def __repr__(self):
        return self.do()

def pick_from_dist(item_prob_dist):
    ranreal = random.random()
    for (ti, prob) in item_prob_dist.items():
        if ranreal < prob:
            return ti 
        else:
            ranreal -= prob
    raise RuntimeError(str(item_prob_dist)+"is not a probability distribution")

env = TP_env()
a = TP_agent(env)
print(a.go(90))