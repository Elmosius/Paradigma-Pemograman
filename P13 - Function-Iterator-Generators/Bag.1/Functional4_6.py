# Coba composite generator

# Fungsi f(x) = x * 2
def f(x):
    return x * 2

# Fungsi g(x) = x + 1
def g(x):
    return x + 1

# Fungsi h(x) = x^2 + 1
def h(x):
    return x**2 + 1

def main():
    # cara 0
    print("0:", [f(x) for x in range(1,11)])
    print()
    # coba cara 1 g(f(x))
    print("1:", [g(f(x)) for x in range(1,11)])
    print()
    # coba cara 2 g(y) for y in f(x)
    print("2:", [g(y) for y in (f(x) for x in range(1,11))])
    print()
    # coba cara 3 simpan dulu di f_x
    f_x = (f(x) for x in range(1,11))
    print("3:", [g(y) for y in f_x])
    
    print("4:", end=" ")
    f_x = (f(x) for x in range(1,11))   # buat ulang
    p = (g(y) for y in f_x)
    for c in p:
        print(c, end=", ")
    print()
    
    # coba cara baru h(g(f(x)))
    print("5:", [h(g(f(x))) for x in range(1,11)])
    print()
    # coba cara baru h(y) for y in g(f(x))
    print("6:", [h(y) for y in (g(f(x)) for x in range(1,11))])
    print()
    # coba cara baru simpan dulu di g_f_x
    g_f_x = (g(f(x)) for x in range(1,11))
    print("7:", [h(y) for y in g_f_x])
    
    print("8:", end=" ")
    g_f_x = (g(f(x)) for x in range(1,11))   # buat ulang
    p = (h(y) for y in g_f_x)
    for c in p:
        print(c, end=", ")
        
if __name__ == "__main__":
    main()
