# File: Kelas06.py
# Penulis : Elmosius Suli
# Default arguments & type hint

class Kelas06:
    # Atribut yang dituliskan Langsung didaLam keLas akan menjadt class member
	# Class member akan dipeLajari nanti

    def	__init__(self, __id: int, name: str = "Noname", _age: int = 30) -> None:
        # "-> None" : type hint, method tidak mengembaLikan niLai
        # "id: int, name: str, _age: int" : type hint, tipe data masing2 argument.
        # "name: str = "Noname", _age: int = 30" : default argument, dipakai jika tidak diisi 
        self.__id =	__id	    # private
        self.name = name        # public
        self._age = _age        # protected

    def cetak(self) -> None:    # -› None = type hint, None = method tidak mengembaLikan apa2 
        print("ID:", self.__id, "| Nama:", self.name, "| Umur:", self._age)
        
## Program utama ##
def main():
    k1 = Kelas06(3, "Hudson Taylor", 20)        
    k2 = Kelas06(4)   
   
    # Coba buka comment baris2 kode int:
    # Error karena td private jadi ttdak bisa dtakses dart Luar keLas
    # print("Print gagaL karena ID private")
    # print("ID:", k1. id, "I Nama:", k1.name, "1 Umur:", k1._age)
    # print("ID:", k2. td, "/ Nama:", k2. name, "1 Umur:", k2._age)
     
    # Ini juga bisa kerena method cetak ada didaLam KeLas06
    print("Panggil method cetak()")
    k1.cetak()
    k2.cetak()


    
if __name__ == '__main__':
    main()
