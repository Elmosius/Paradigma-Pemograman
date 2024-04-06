# Belajar Tuples

def main():
    # bisa tanpa tanda kurung ()
    stock1= "APPL", 123.52, 137.98, 53.15
    # lebih disarankan selalu menggunakan tanda kurung ()
    stock2= ("APPL", 123.52, 137.98, 53.15)
    print("stock1: ", stock1);
    print("stock2: ", stock2);
    
    # Tuple immutable, tidak bisa diubah
    # coba uncomment, dan jalankan baris di bawah
    # stock1[0] = "0000"
    
    # Akses tuple dengan indeks-nya
    print("stock[1]: ", stock1[1])
    
    # Akses tuple menggunakan slicing [1:3] dari indeks 1 sampai indeks 3,
    # indeks 3 sendiri tidak termasuk
    print("stock1[1:3]: ", stock1[1:3])
    
if __name__ == "__main__":
    main()