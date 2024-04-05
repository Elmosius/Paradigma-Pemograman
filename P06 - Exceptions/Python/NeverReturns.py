# Exception: menunjukkan exception langsung menghentikan program
# tanpa mengeksekusi perintah selanjutnya.

from typing import NoReturn

class NeverReturns:
    def never_returns(self) -> NoReturn:
        print("Method never_returns akan me-raise exception:")
        raise Exception("Exception ini akan selalu dijalankan/ terjadi")
        print("Perintah print ini tidak akan pernah dieksekusi")
        return("Perintah return ini juga tidak akan pernah dieksekusi")
    
def main():
    nr = NeverReturns()
    nr.never_returns()
    
if __name__ == "__main__":
    main( )    
    