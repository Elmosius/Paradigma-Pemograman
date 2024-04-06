# Dictionary02

def main():
    d1 = dict(red=128, green=128, blue=128)
    d2= {'red':128, 'green':128, 'blue':128}
    print("d1: ", d1)
    print("d2: ", d2)
    
    
    # Menggunakan method get()
    print("d1.get('red'):", d1.get('red'))
    print("d1.get('kuning'): ", d1.get('kuning'))
    print("d1.get('kuning', 170): ", d1.get('kuning', 170))
    print("d1.get('kuning'): ", d1.get('kuning'))
    
    # Menggunakan setDefault()
    d1.setdefault('kuning', 200)
    print("d1.get('kuning'): ", d1.get('kuning'))
    
    #setDefault itdak mengubah data yg sudah ada
    d1.setdefault('blue', 200)
    print("d1.get('blue'): ", d1.get('blue'))
    
    
if __name__ == "__main__":
    main()