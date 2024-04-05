# Exception: penggunaan else & finally

class HandlingExceptions5:
        def coba_else_finally(self) -> None:
            some_exceptions = [ValueError, TypeError, IndexError, None]
            
            for choice in some_exceptions:
                try:
                    print(f"\nRaising {choice}")
                    if choice:
                        raise choice("Terjadi exception")
                    else:
                        print("Tidak ada exception yg di raise")
                        
                except ValueError:
                    print("Menangkap ValueError exception")
                    
                except TypeError:
                    print("Menangkap TypeError exception")
                except Exception as e:  # menangkap semua exception lain
                    print(f"Menangkap exception lain: {e.__class__.__name__}")
                else:
                    print("Kode ini dijalankan jika tidak terjadi exception")
                finally:
                    print("Kode di finally selalu dijalankan")
                    
def main():
    he = HandlingExceptions5()
    he.coba_else_finally()
    
if __name__ == "__main__":
    main( )   