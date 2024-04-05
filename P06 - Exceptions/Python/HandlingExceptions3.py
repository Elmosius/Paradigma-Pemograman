# Exception: menangani beberapa exception (ZeroDivisonError, TypeError)
# untuk ValueError masih belum ditangani

from typing import Union

class HandlingExceptions3:
        def funny_division(self, divisor: int) -> Union[str,float]:
            try:
                if divisor == 13:
                    raise ValueError("Angka 13 tidak diperbolehkan")
                return 100/ divisor
            
            except(ZeroDivisionError, TypeError):
                return("Masukkan sebuah bilangan yang bukan nol")
            
            
def main():
    he = HandlingExceptions3()
    for val in(20.0,0,"hello",13):
        # end: ganti newline dg ": " supaya bersambung dg print berikutnya
        print(f"Testing {val!r}", end=": ")
        print(he.funny_division(val))
    
if __name__ == "__main__":
    main( )   