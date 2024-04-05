# File: Kelas07.py
# Penulis : Elmosius Suli
# Method __str__ yg dipanggil otomatis ketika mencetak objek secara langsung

class Kelas07:
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
        
    def __str__(self) -> str:
        # method dipanggil otomatis ketika mencetak objek secara langsung
        return "ID: %d | Nama: %s | Umur: %d" % (self.__id, self.name, self._age)
        
## Program utama ##
def main():
    k1 = Kelas07(3, "Hudson Taylor", 20)        
    print("Panggil method cetak()")

    k1.cetak()
    print("\nCetak objek langsung, method __str__() otomatis digunakan.")
    print("Print obj: ", k1)       # Langsung cetak objek
    print("Hasil str: ", str(k1))  # Cetak objek secara explisit memanggil method str()
    
if __name__ == '__main__':
    main()
