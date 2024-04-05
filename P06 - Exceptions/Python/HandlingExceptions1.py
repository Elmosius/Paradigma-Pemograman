# Exception: cara menghandle exception sehingga dapat diatur supaya dapat
# mengeluarkan pesan kesalah dan menlanjutkan program, tidak langsung keluar


from NeverReturns import NeverReturns

class HandlingExceptions1:
        def handler(self) -> None:
            nr = NeverReturns()
            try:
                nr.never_returns()
            except Exception as ex: # Bisa menangkap semua jenis exception, ex = obj
                print(f"Exception tertangkap: {ex!r}") # 2 format yg berbeda
                print(f"Exception tertangkap: {ex}")  # dari exception yg sama
            print("Perintah yg dieksekusi setelah terjadi exception")
            
def main():
    he = HandlingExceptions1()
    he.handler()
    print("Perintah yg dieksekusi selanjutnya")
    
if __name__ == "__main__":
    main( )   