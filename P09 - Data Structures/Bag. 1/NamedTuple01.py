# Belajar Named Tuple
from dataclasses import dataclass
from typing import Optional
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

@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float

def main():
    # Menggunakan urutan (positions)
    t1 = Stock("APPL", 123.52, 137.98, 53.15)
    print("t1: ", t1)
    
    # Menggunakan atribut
    t2 = Stock("APPL", low=123.52, high=137.98, current=53.15)
    print("t2: ", t2)
    
    # Akses menggunakan atribut
    print("t1.symbol:   ", t1.symbol)
    print("t1.current:   ", t1.current)
    print("t1.high:   ", t1.high)
    print("t1.low:   ", t1.low)

    # Coba dengan nilai default
    d1 = StockDefaults("GOOG")
    d2 = StockDefaults("GOOG", 1826.77, 1847.20, 1013.54)
    print("d1: ", d1)
    print("d2: ", d2)

    # Coba terurut
    d3 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
    d4 = StockOrdered("GOOG")
    d5 = StockOrdered("GOOG", 1726.77, 2047, 2013.54)
    print("Ordered Stocks:")
    pprint(sorted([d3, d4, d5]))

    # Coba frozen, coba buka baris yang dikomentari akan error
    d6 = StockFrozen("GOOG", 100.00, 200.20, 50.30)
    # d6.current = 150.10

if __name__ == "__main__":
    main()
