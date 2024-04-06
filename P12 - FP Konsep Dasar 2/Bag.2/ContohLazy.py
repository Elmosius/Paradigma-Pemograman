class ContohLazy:
    def __init__(self, limit):
        self.limit = limit
    
    def lazy_evaluation(self):
        return (x**2 for x in range (self.limit))