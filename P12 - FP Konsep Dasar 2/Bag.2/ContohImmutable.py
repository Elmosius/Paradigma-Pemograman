# Immutable adalah data yang tidak dapat diubah
class ContohImmutable:
    def __init__(self, values):
        self.values = tuple(values)         # tuple merupakan type data yang immutable

    def get_values(self): 
        return self.values

    def change_value(self, new_value):
        # Akan menghasilkan error karena tuple tidak dapat diubah
        self.values += (new_value)