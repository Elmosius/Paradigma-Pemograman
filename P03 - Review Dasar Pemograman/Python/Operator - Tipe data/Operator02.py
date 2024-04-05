# Opeator Aritmetik

def main():
    # Identity operator 'is' & 'is not'
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    
    print("x : ", x)
    print("y : ", y)
    print("z : ", z)
    print("x is z : ", x is z)
    # True karena z objek yg sama dengan x
    print("x is not z : ", x is not z)
    print("x is y : ", x is y)
    # False karena x pbjek yg berbeda gh y, meskipun isinya sama
    print("x == y : ", x == y)
    # "is" berbeda dengan "=="
    print()
    
    # Operator membership 'in' & 'not in'
    a = "pinguin"
    b = "dolphin"
    c = ["shark", "walrus", "pinguin"]
    d = ("shark", "walrus", "pinguin")
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print("a in c = ", a in c)
    print("a not in c = ", a not in c)
    print("b in c = ", b in c)
    print("a in d = ", a in d)
    print("b in d = ", b in d)
    
    # Fungsi isinstance()
    a = 300
    print("isinstance(a, int) : ", isinstance(a, int))
    # Mengecek apakah sebuah objek berasal dari kelas/tipe tertentu
    
if __name__ == "__main__":
    main()            