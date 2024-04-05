# File: Kelas04.py
# Penulis : Elmosius Suli
# Membuat atribut didaLam keLas & initiaLizer

class Kelas04:
    # Atribut yang dituLiskan Langsung didaLam keLas akan menjadi class member
    # CLass member akan dipeLajari nanti

    def __init__(self):
        # InitiaLizer untuk mengisi niLai awaL kedaLam atribut2
        # Otomatis dijaLankan ketika membuat objek
        # Buat atribut2 didaLam initiaLizer
        self.__id: int = 1          # private
        self.name: str = "Nama1"    # public
        self._age: int = 21         # protected

    def cetak(self):
        print("ID: ", self.__id, "| Nama: ",self.name,"| Umur: ", self._age)
        
## Program utama ##
def main():
    k1 = Kelas04()              # k1 = objek dari Kelas04
    k1.cetak()
    
    # Jangan isi data ke atribut private dart Luar keLas tsb,
	# karena Python akan membuatkan atribut Baru dg nama soma
	# kl. id = 3

    
    print("Setelah data diubah: ")
    k1.name = "Hudson Taylor" # yg bukan private boleh
    k1._age = 20
    k1.cetak()
    
if __name__ == '__main__':
    main()
