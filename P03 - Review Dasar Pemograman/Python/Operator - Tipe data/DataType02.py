# Buat variable menggunakan constructor functions

def main():
    var = str("Python mudah dipelajari.") 
    print("Tipe:", type(var)," Data:",var)

    var = int (37) 
    print("Tipe:", type(var)," Data: ",var)

    var = float(3.14)
    print("Tipe:", type (var)," Data: ",var)

    var = complex(5+ 2j)
    print("Tipe:", type (var)," Data:",var)
    var = list(("alpukat", "durian", "strawberry")) 
    print("Tipe:", type (var)," Data: ",var)

    var = tuple(("mangga", "nanas", "jambu", "nangka")) 
    print("Tipe:", type(var)," Data: ",var)

    var = range(3, 20, 2)
    print("Tipe:", type (var)," Data:",var)

    var =dict(nama = "Joshua", umur = 17) 
    print("Tipe:", type (var)," Data:",var)

    var = set(("Brazil", "Rusia", "India", "China", "South Africa")) 
    print("Tipe:", type(var)," Data:",var)

    var = frozenset(("es", "ikan beku", "daging beku")) 
    print("Tipe:", type(var)," Data:",var)

    var = bool (3)
    print("Tipe:", type(var)," Data:",var)

    var =bytes(7)
    print("Tipe:", type (var)," Data:",var)

    var = bytearray(3) 
    print("Tipe:", type(var)," Data:",var)

    var = memoryview(bytes (3))
    print("Tipe:", type (var)," Data:",var)
    
if __name__ == "__main__":
    main()            