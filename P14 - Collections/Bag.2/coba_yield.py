# Coba yield and return

def fungsi_return():
    for c in range(5):
        return c
    
def fungsi_yield():
    for c in range(5):
        yield c
    return

def fungsi_yield2():
    for c in range(5):
        yield from(x for x in range(c))
    return

def main():
    print("Panggil fungsi_return():")
    print(list([fungsi_return()]))
    
    print("Panggil fungsi_yield():")
    print(list(fungsi_yield()))
    
    print("Panggil fungsi_yield2():")
    print(list(fungsi_yield2()))
    
if __name__ == '__main__':
    main()