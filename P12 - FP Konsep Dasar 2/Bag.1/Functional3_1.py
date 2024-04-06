# Recursion instead of an explicit loop state
# Test bilangan prima.
# coprime: dua bilangan hanya memiliki angka 1 sebagai faktor yg sama
# prima = not any(n % p == 0 for in range(2, int(math.sqrt(n))+1))
import math

# fungsi test prima cara rekursif
import sys

def isprimer(n: int)-> bool:
    def isprime(k: int, coprime: int)-> bool:
        '_Is k relatively prime to the value coprime?'
        if k < coprime*coprime: return True
        if k % coprime == 0: return False
        return isprime(k,coprime+2)
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n,3)

# Fungsi dengan Tail Cail Optimization
# (recursive -> loop) / generator expression
def isprimei(n: int)-> bool:
    if n< 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,1+int(math.sqrt(n)),2):
        if n % i == 0: return False
    return True
  
def main():
    print("Recursion limit: ", sys.getrecursionlimit())
    
    print("Bilangan prima < 20")
    for c in range(2,20):
        if isprimer(c):
            print(c, end=" ")
    print()
    
    for c in range(2,20):
        if isprimei(c):
            print(c, end=" ")
    print()
    
    print([x for x in range(3,20)if isprimei(x)])
    print(tuple((x, isprimei(x)) for x in range(3,10)))
    
if __name__ == "__main__":
    main()