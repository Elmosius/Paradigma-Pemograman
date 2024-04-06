# Mutable adalah type data yang dapat diubah
class ContohMutable:
    def __init__(self, values):
        self.values = list(values)      # list merupakan type data yang mutable

    def get_values(self):
        return self.values

    def change_value(self, new_value):
        self.values.append(new_value)   # sehingga list dapat diubah dengan memanggil fungsi append