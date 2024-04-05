# File: Kelas10.py
# Penulis : Elmosius Suli
# Destruktor (method yg otomatis dipanggil ketika Garbage Collector menghapus objek)

import datetime

class Kelas10:
    def __init__(self, age):
       self.__age = age
    
    def __del__(self):
        # destruktor yg akan dipanggil ketika objek sedang dihancurkan oleh GC
        print("Destruktor sedang dijalankan: ", self.__age)
        
    @property
    def age(self):          # accessor
        return self.__age

    @age.setter 
    def age(self, age:int): # mutator
        self.__age = age
        
## Program utama ##
def main():
    k1 = Kelas10(21)           # membuat objek k dari kelas10
    print("Age: ", k1.age)     # berhasil, lewat accessor / getter
    del(k1)                   
    
    k2 = Kelas10(19)           # membuat objek k dari kelas10
    print("Age: ", k2.age)     # berhasil, lewat accessor / getter
    k3 = k2                    # k2 & k3 menunjuk ke objek yg sama (2 petunjuk)
    print("Lepas penunjuk k2...")
    
    k2 = None                  # k2 dilepas, masih ada k3, objek belum di hapus
    print("Age: ", k3.age)
    print("Lepas penunjuk k3...")
    
    k3 = None                  # k3 dilepas, tidak ada penunjuk, objek akan dihapus oleh GC
    # print ("Age: ", k3.age)  # jika diaktifkan akan error karena objek sudah dihapus oleh GC 
if __name__ == '__main__':
    main()
