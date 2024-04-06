# Belajar Named Tuple
from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float
    
def main():
    # Menggunakan urutan (positions)
    t1 = Stock("APPL", 123.52, 137.98, 53.15)
    print("t1: ", t1)
    
    # Tambah member tuple, penambahan harus tuple juga
    t2 = t1.__add__((11.22, 33.44))
    print("t2: ", t2)
    
    # Ukuran tuple
    print("len(t1): ", len((t1)))
    print("len(t2): ", len((t2)))
    
    t3 = Stock("APPL", 123.52, 137.98, 53.15)
    t4 = Stock("APPL", 123.52, 137.98, 11.22)
    print("t3: ", t3)
    print("t4: ", t4)
    
    
    # Cek kesamaan bisa pakai ==
    if (t1 == t3):
        print("t1 == t3")
    else:
        print("t1 != t3")
        
    # Cek kesamaan bisa pakai __eq__()
    if t1.__eq__(t3):
        print("t1 == t3")
    else:
        print("t1 != t3")
        
    # Cek kesamaan bisa pakai ==
    if (t1 == t4):
        print("t1 == t4")
    else:
        print("t1 != t4")
        
        
    # Cek kesamaan bisa pakai __eq__()
    if t1.__eq__(t4):
        print("t1 == t4")
    else:
        print("t1 != t4")
    
if __name__ == "__main__":
    main()