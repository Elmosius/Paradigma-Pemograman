# Belajar Named Tuple
from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float
    
    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2
    
    @property
    def price_range(self) -> float:
        return self.high - self.low

def main():
    # Menggunakan urutan (positions)
    t1 = Stock("APPL", low=123.52, high=137.98, current=53.15)
    print("t1: ", t1)
    
    # Akses menggunakan atribut
    print("t1.symbol:   ", t1.symbol)
    print("t1.current:   ", t1.current)
    print("t1.high:   ", t1.high)
    print("t1.low:   ", t1.low)
    
    # Akses atribut turunan (hasil perhitungan)
    print("t1.middle: ", t1.middle)
    
    # Akses property baru
    print("t1.price_range: ", t1.price_range)

if __name__ == "__main__":
    main()
