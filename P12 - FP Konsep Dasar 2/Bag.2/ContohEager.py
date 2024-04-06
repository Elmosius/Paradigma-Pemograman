class ContohEager():
    def __init__(self, limit):
        self.limit = limit

    def eager_evaluation(self):
        return [x**2 for x in range (self.limit)]