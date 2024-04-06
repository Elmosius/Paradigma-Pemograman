# Pure function & non-pure function

class CobaPureFunction:
    def __init__(self) -> None:
        self.attr1: int = 0
    
    # pure function
    def tambah(self,a: int, b:int) -> int:
        return a+b

    # non-pure fucntion (ringan)
    def kurang(self,a: int, b: int)-> int:
        c = a-b
        return c
    
    # non-pure function (loop state)
    def kali(self,a:int, b:int)-> int:
        hasil = 0
        for c in range(b):
            hasil = hasil +a
            print("perubahan state, hasil:", hasil)
        return hasil
    
    # non-pure function (state change)
    def counter(self, n:int):
        print("di counter, n:", n," attr1:", self.attr1)
        self.attr1 = self.attr1+n
        print("di counter, n:", n," attr1:", self.attr1)
        return self.attr1

    # new non-pure function (I/O operation)
    def print_hello(self):
        print("Hello, world!")
        return None

def main():
    c = 7
    d = 3
    cp = CobaPureFunction()
    cp.attr1 = 5
    print(cp.tambah(c,d))
    print(cp.kurang(c,d))
    print(cp.kali(c,d))
    print("di main, attr1 (sebelum):", cp.attr1)
    print(cp.counter(d))
    print("di main, atrr1 (sesudah):", cp.attr1)
    cp.print_hello()  # new function call

if __name__ == "__main__":
    main()
