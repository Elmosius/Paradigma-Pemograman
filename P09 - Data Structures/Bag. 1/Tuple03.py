# Belajar Tuples

def main():
    # Tuple dengan 1 item, harus tulsi tanda koma
    t1= 38,
    print("t1: ", t1)
    print("t1 class: ", t1.__class__)
    
    # Tanpa tanda koma, jadi bilangan biasa bukan tuple
    t2= 39
    print("t2: ", t2)
    print("t2 class: ", t2.__class__)
    
    # Tuple di dalam tuple (2 tingkat)
    t3= ((1,2), (3,4))
    print("t3: ", t3)
    print("t3 class: ", t3.__class__)
    print("t3[1]: ", t3[1])
    print("t3[1] class: ", t3[1].__class__)
    
    # Tuple kosong
    t4 = ()
    print("t4: ", t4)
    print("t4 class: ", t4.__class__)
    
    # Tuple dengan empat tingkat 
    t5 = (1, ('a', (4.0, ('x', 'y', 'z'))))
    print("\nTuple dengan empat tingkat (menggunakan tuple bersarang):")
   
    # Mengakses elemen di setiap tingkat
    level1 = t5[0]
    print("Level 1:", level1)

    level2 = t5[1]
    print("Level 2:", level2)

    # Mengakses elemen di dalam tuple tingkat kedua
    level2_tuple = level2[1]
    print("Level 2 Tuple:", level2_tuple)

    # Mengakses elemen di dalam tuple tingkat ketiga
    level3_tuple = level2_tuple[1]
    print("Level 3 Tuple:", level3_tuple)

    # Mengakses elemen di dalam tuple tingkat keempat
    level4_element = level3_tuple[2]
    print("Level 4 Element:", level4_element)

if __name__ == "__main__":
    main()



