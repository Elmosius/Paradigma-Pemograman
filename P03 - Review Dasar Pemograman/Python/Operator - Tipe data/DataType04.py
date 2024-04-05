# Konversi tipe data

def main():
    # int()
    a = int(5)
    b = int(3.5)
    c = int("7")
    d = int('15')
    # e = int("3.14")   # ValueError : invalid literal for int() with base 10: '3.14'
    # f = int(2j)
     
    print("a = ", a, ", tipe: ", type(a))
    print("b = ", b, ", tipe: ", type(b))
    print("c = ", c, ", tipe: ", type(c))
    print("d = ", d, ", tipe: ", type(d))
    print()
    
    # float()
    a = float(8)
    b = float(12.5)
    c = float("10")
    d = float('14.7')
    # e = float(3j)     # TypeError : can't convert complex to float
    print("a = ", a, ", tipe: ", type(a))
    print("b = ", b, ", tipe: ", type(b))
    print("c = ", c, ", tipe: ", type(c))
    print("d = ", d, ", tipe: ", type(d))
    print()
    
    # String
    a = str(14)
    b = str(12.34)
    c = str("hallo")
    d = str('Python')
    e = str(4j)
       
    print("a = ", a, ", tipe: ", type(a))
    print("b = ", b, ", tipe: ", type(b))
    print("c = ", c, ", tipe: ", type(c))
    print("d = ", d, ", tipe: ", type(d))
    print("e = ", e, ", tipe: ", type(e))
    print()
    
if __name__ == "__main__":
    main()            