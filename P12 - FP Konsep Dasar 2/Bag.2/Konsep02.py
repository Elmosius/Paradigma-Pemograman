# Dalam functional programming, kita dapat menggunakan lambda
# Lambda adalah sebuah fungsi yang tidak diberikan nama (Hanya dimasukan kedalam sebuah variabel)
# Lambda fungsi ini biasanya digunakan untuk membuat fungsi yang simple (hanya 1 baris)

def main():
    # Membuat lambda expressions
    tambah = lambda x, y: x + y     # lambda expressions ini dimasukan kedalam variabel 'tambah'
    kali = lambda x, y: x * y       # lambda expressions ini dimasukan kedalam variabel 'kali'
    bagi = lambda x, y: x / y       # lambda expressions ini dimasukan kedalam variabel 'bagi'

    print(tambah(1, 2))             # untuk memanggil lambda expression, sama seperti fungsi biasa
    print(kali(1, 2))
    print(bagi(1, 2))

    print(tambah.__code__.co_varnames)  # karena lambda expression sebenarnya adalah sebuah fungsi,
                                        # kita dapat mengambil atribut-atribut sama seperti fungsi yang biasa

if __name__ == "__main__":
    main()