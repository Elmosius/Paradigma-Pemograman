# File: Kelas05.py
# Penulis : Elmosius Suli
# Initializer yang menerima parameter

class Kelas05:
    # Atribut yang dituliskan Langsung didaLam keLas akan menjadt class member
	# Class member akan dipeLajari nanti

    def __init__(self, __id: int, name: str, _age: int):
        self.__id = __id   # private
        self.name = name   # public
        self._age = _age   # protected

    def cetak(self):
        print("ID: ", self.__id, "| Nama: ",self.name,"| Umur: ", self._age)
        
## Program utama ##
def main():
    k1 = Kelas05(3, "Hudson Taylor", 20)        # k1 = objek dari Kelas05
    k2 = Kelas05(4, "Abraham Lincoln", 33)      # k2 - objek dari Kelas05 juga
   
    # Coba buka comment baris2 kode int:
    # Error karena td private jadi ttdak bisa dtakses dart Luar keLas
    # print("Print gagaL karena ID private")
    # print("ID:", k1. id, "I Nama:", k1.name, "1 Umur:", k1._age)
    # print("ID:", k2. td, "/ Nama:", k2. name, "1 Umur:", k2._age)
     
    # KaLau int bisa
    print("Print tanpa ID")
    print("Nama:", k1.name, "I Umur:", k1._age)
    print("Nama:", k2.name, "I Umur:", k2._age)
    
    # Ini juga bisa kerena method cetak ada dtdaLam KeLasO5
    print("Panggil method cetak()")
    k1.cetak()
    k2.cetak()

    
if __name__ == '__main__':
    main()
