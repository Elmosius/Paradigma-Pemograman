# File TestHewanReptilUNggas.py

from Hewan import Hewan
from Reptil import Reptil
from Unggas import Unggas

def main():
    satwa = Hewan()
    cicak = Reptil()
    ayam = Unggas()
    
    print("Yang menjadi ciri satwa")
    satwa.bernafas()
    satwa.berkembang_biak()
    print()
    
    print("Yang menjadi ciri cicak:")
    cicak.bernafas()
    cicak.berkembang_biak()
    cicak.melata()
    print()
    
    
    print("Yang menjadi ciri ayam:")
    ayam.bernafas()
    ayam.berkembang_biak()
    ayam.berparuh()
    print()
    
if __name__ == "__main__":
    main()