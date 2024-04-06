# Dictionary03

def main():
    d1 = dict(red=100, green=200, blue=255)
    d2= {'red':250, 'green':150, 'blue':110}
    print("d1: ", d1)
    print("d2: ", d2)
    
    
    # Coba keys(), values(), items()
    print("d1.keys(): ", d1.keys())
    print("d1.values(): ", d1.values())
    print("d1.items(): ", d1.items())
    for warna, nilai in d2.items():
        print(f"{warna} bernilai {nilai}")
    
    
if __name__ == "__main__":
    main()