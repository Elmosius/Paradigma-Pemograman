# File: Kelas08.py
# Penulis : Elmosius Suli
# Accessor & Mutator (getter & setter method)

class Kelas08:
    def __init__(self, age):
       self.__age = age
    
    @property
    def age(self):          # accessor
        return self.__age

    
    @age.setter 
    def age(self, age:int): # mutator
        self.__age = age
        
## Program utama ##
def main():
    k = Kelas08(21)
    # print("Age: ", k.__age) # error karena __age private
    
    print("Age: ", k.age)     # berhasil, lewat accessor / getter
    k.age = 17                # berhasil, lewat mutator / setter
    print("Age: ", k.age)    
    
if __name__ == '__main__':
    main()
