class Agent(object):
    def __init__(self, env):
        """ set up the agent"""
        self.env = env

    def go(self, n):
        # acts for n time setps
        raise NotImplementedError("go")


class TP_env(object):
    def __init__(self):
        self.time = 0
        self.stock = 20

    def do(self, action):

        return {'price': price, 'instock': self.stock}
