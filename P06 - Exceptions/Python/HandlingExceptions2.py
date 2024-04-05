# Exception: menangani 1 exception secara spesifik
# Hal ini lebih baik, tetapi exception lain akan lolos

from typing import Union

class HandlingExceptions2:
        # Union: gabungan, output bisa berupa str atau float
        def funny_division(self, divisor: float) -> Union[str,float]:
            try:
                return 100/ divisor
            except ZeroDivisionError:
                return "Tidak bisa membagi dengan nol"
            
def main():
    he = HandlingExceptions2()
    # Normal, tidak terjadi exception
    print("5: " + str(he.funny_division(5)))
    # Exception tertangkap karena sesuai except
    print("0: " + he.funny_division(0))
    # Exception tidak tertangkap, coba di uncomment
    # print("hallo:" + he.funny_division("hallo"))
    print("Perintah di main() yg dieksekusi selanjutnya...")
    
if __name__ == "__main__":
    main( )   