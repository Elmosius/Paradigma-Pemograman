# Belajar Named Tuple
from dataclasses import dataclass
from pprint import pprint

@dataclass
class StockDefaults:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
   
@dataclass(order=True)
class StockOrdered:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
    
@dataclass(frozen=True)
class StockFrozen:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
    
def main():
    # Coba dengan nilai default
    d1 = StockDefaults("GOOG")
    d2 = StockDefaults("GOOG", 1826.77, 1847.20, 1013.54)
    print("d1: ", d1)
    print("d2: ", d2)
    
    # Coba terurut
    d3 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
    d4 = StockOrdered("GOOG")
    d5 = StockOrdered("GOOG", 1726.77, 2047, 2013.54)
    pprint(sorted([d3,d4,d5]))
    
    # Perbandingan
    print("d3 < d4: ", d3 < d4)
    print("d3 > d4: ", d3 > d4)
    
    # Coba frozen, coba buka baris yg dikomentari akan error
    d6 = StockFrozen("GOOG", 100.00, 200.20, 50.30)
    # d6.current = 150.10
    
if __name__ == "__main__":
    main()