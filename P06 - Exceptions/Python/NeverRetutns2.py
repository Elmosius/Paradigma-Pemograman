# Exception: menunjukkan exception langsung menghentikan program
# tanpa mengeksekusi perintah selanjutnya termasuk jika dipanggil
# dari program / fungsi lain.

from NeverReturns import NeverReturns

class NeverReturns2:
    def call_exceptor(self) -> None:
        print("Method ini akan memanggil method never_returns():")
        nr = NeverReturns()
        nr.never_returns()
        print("Method never_returns() menghasilkan exception, ")
        print("sehingga kode berikutnya dari pemanggil tidak akan dijalankan.")
        
        
def main():
    nr2 = NeverReturns2()
    nr2.call_exceptor()
    
if __name__ == "__main__":
    main( )    
    