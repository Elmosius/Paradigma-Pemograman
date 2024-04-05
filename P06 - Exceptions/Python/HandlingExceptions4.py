# Exception: menangkap beberapa exception
from typing import Union

class HandlingExceptions4:
        def funny_division(self, divisor: int) -> Union[str,float]:
            try:
                if divisor == 13:
                    raise ValueError("Angka 13 tidak diperbolehkan")
                return 100/ divisor
            except ZeroDivisionError:
                return("Masukkan angka selain nol")
            except TypeError:
                return("Masukkan bilangan, bukan yg lain")
            except ValueError:
                print("Jangka angka 13")
                raise   # Melempar ulang exception yg terjadi
def main():
    he = HandlingExceptions4()
    for val in(20.0,0,"hello",13):
        print(f"Testing {val!r}", end=": ")
        print(he.funny_division(val))
    
if __name__ == "__main__":
    main( )   