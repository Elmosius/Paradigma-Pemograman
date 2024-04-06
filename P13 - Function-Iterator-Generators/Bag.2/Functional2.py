# Pure fucntions pada Python merupakan sebuah function yang tidak memiliki side effects
# dan dapat dipastikan dengan input yang sama, output function tersebut akan tetap sama

# Contoh pure function
def pangkat(x, y):
    return x ** y

# Contoh impure function
angka = 2   # Variabel global

def cthInpure(x):
    return x + angka

def main():
    # Pure function akan memiliki output yang sama, dengan input (parameter) yang sama
    print(pangkat(2,2))
    print(pangkat(2,2))
    
    # Inpure function belum tentu memiliki output yang sama walau dengan parameter yang sama
    # Hal ini dikarenakan inpure function memiliki side effect
    # side effect dalam functional programming adalah kondisi dimana output dari sebuah function
    # Bergantung dengan hal yang ada di luar function tersebut (seperti variabel global)
    print(cthInpure(5)) # 7
    global angka
    angka = 3
    print(cthInpure(5)) # 8
if __name__ == "__main__":
    main()