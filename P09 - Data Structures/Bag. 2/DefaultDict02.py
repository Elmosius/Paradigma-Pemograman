import collections
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint

# Dataclass sebgai fungsi custom untuk defaultdict
# semua atribut harus punya nilai default
@dataclass
class Prices:
    current: float = 0.0
    high: float = 0.0
    low:float = 0.0
    
    
# Fungsi pendukung harga stock di group berdasarkan bulan
def make_defaultdict():
    return collections.defaultdict(Prices)

def main():
    # Prices sebagai default value untuk defaultdict
    print("Prices sebagai default value untuk defaultdict: ")
    portfolio = defaultdict(Prices)
    portfolio["AAPL"] = Prices(current=122.25, high=137.98, low=53.15)
    portfolio["GOOG"]
    portfolio["HUAW"]
    
    for key, value in portfolio.items():
        print("key: ", key, ", value: ", value)
        
    # print dengan cara lain
    pprint(portfolio)
    
    # Harga stock di group berdasarkan bulan
    print("\nHarga stock di group berdasarkan bulan:")
    by_month = collections.defaultdict(lambda: make_defaultdict())
    by_month["APPL"]["Jan"] = Prices(current=122.25, high=137.98, low=53.15)
    by_month["APPL"]["Feb"]
    by_month["HUAW"]["Jan"]

    for key1, val1, in by_month.items():
        for key2, val2 in val1.items():
            print("key1: ", key1, ", key2: ", key2, ", value: ", val2)
    pprint(by_month)
    
if __name__ == "__main__":
    main()
