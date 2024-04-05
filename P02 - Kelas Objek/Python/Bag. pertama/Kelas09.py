# File: Kelas08.py
# Penulis : Elmosius Suli
# Behavior / method & pembuatan objek

import datetime

class Kelas09:
    def __init__(self, age):
       self.__age = age
    
    def computeYob(self) -> int:    # method hitung tahun kelahiran
        now = datetime.datetime.now()
        return now.year - self.__age
    
    @property
    def age(self):          # accessor
        return self.__age

    
    @age.setter 
    def age(self, age:int): # mutator
        self.__age = age
        
## Program utama ##
def main():
    k = Kelas09(21)           # membuat objek k dari kelas09
        
    print("Age: ", k.age)     # berhasil, lewat accessor / getter
    print("Tahun lahir: ", k.computeYob())
    k.age = 17                # berhasil, lewat mutator / setter
    print("Age: ", k.age)    
    print("Tahun lahir: ", k.computeYob())
    
if __name__ == '__main__':
    main()
