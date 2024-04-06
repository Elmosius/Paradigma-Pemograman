# Fungsi dalam Python adalah first-class objects
# Itu berarti bahwa fungsi dalam Python sebenarnya adalah sebuah object
# Sehingga terdapat beberapa atribut dalam fungsi tersebut yang dapat kita ambil

def testFunction(a: int, b: str, c: float = 0.0) -> bytes:
    pass

def main():
    print(type(testFunction))   # function dalam Python merupakan object dari class 'function'

    print(testFunction.__code__.co_argcount)    # mengambil jumlah argumen pada sebuah function
    print(testFunction.__code__.co_varnames)    # mengambil argumen-argumen pada sebuah function dalam bentuk Tuple
    print(testFunction.__defaults__)    # mengabil default values dari parameter function

if __name__ == "__main__":
    main()
