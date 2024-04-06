# Higher order functions merupakan konsep dimana sebuah fungsi dapat
# menerima fungsi lain sebagai parameter atau mengembalikan fungsi lain

def pangkat(x: int):
    return x**2

def main():
    # salah satu contoh high order function bawaan Python adalah map()
    # map() menerima sebuah fungsi dan sebuah iterable (List atau Tuple)

    angka = [1, 2, 3, 4, 5]
    
    processed = map(lambda x: x**2, angka) # di contoh ini, kita menggunakan lambda expression langsung
                                            # pada parameter 1 map() yang menerima fungsi

    processed2 = map(pangkat, angka)    # di contoh ini, kita menggunakan fungsi yang kita buat sendiri sebagai parameter
                                        # ketika kita mengirimkan fungsi sebagai parameter, kita tidak menyertakan () nya

    # processed2 = map(pangkat(), angka)    # error, karena pangkat() malah akan memanggil fungsinya

    print(list(processed))
    print(list(processed2))

if __name__ == "__main__":
    main()