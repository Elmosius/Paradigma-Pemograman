# Assign value dan cek tipe-nya

def main():
    var = ("Belajar Python kerennn....") 
    print("Tipe:", type(var)," Data:",var)
    
    var = 17
    print("Tipe:", type(var)," Data:",var)
    
    var = 3.14
    print("Tipe:", type(var)," Data:",var)
    
    var = 3 + 1j 
    print("Tipe:", type(var)," Data: ",var)
    
    
    var = ["alpukat", "durian", "strawberry"] 
    print("Tipe:", type(var)," Data:",var)
    
    var = ("mangga", "nanas", "jambu", "nangka")
    print("Tipe:", type(var)," Data:",var)
    
    var = range(3, 20, 2)
    print("Tipe:", type(var)," Data:",var)
    
    var = {"nama": "Joshua", "umur": 17}
    print("Tipe:",type(var)," Data:",var)
    
    var = {"Brazil", "Rusia", "India", "China", "South Africa"} 
    print("Tipe:", type(var)," Data:",var)
    
    var = frozenset({"es", "ikan beku", "daging beku"}) 
    print("Tipe:", type (var)," Data:",var)
    
    var = True
    print("Tipe:", type(var)," Data:",var)
    
    var = b"mobil listrik"
    print("Tipe:", type(var)," Data:",var)
    
    var = bytearray(3)
    print("Tipe:", type(var)," Data:",var)
    
    var = memoryview(bytes(7)) 
    print("Tipe:", type(var)," Data: ",var)
    
    var = None
    print("Tipe:", type(var)," Data:",var)
    
if __name__ == "__main__":
    main()            