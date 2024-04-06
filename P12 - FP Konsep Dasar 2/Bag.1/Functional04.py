# Fungsi sebagai first class member

def tambah(a: int, b: int) -> int:
    return a + b

def kurang(a: int, b: int) -> int:
    return a - b

def kali(a: int, b: int) -> int:
    return a * b

def bagi(a: int, b: int) -> int:
    return a / b

def prosesor(func, a: int, b: int) -> int:
    # Fungsi sebagai parameter & sebagai return
    return func(a, b)

def prosesor2(func, a: int, b: int) -> int:
    # Fungsi sebagai parameter & sebagai return
    z = func()
    return z(a, b)

def dummy_error(a: int, b: int) -> int:
    print("Fungsi tidak ada!")
    return -99999

def pilih_operasi():
    p = int(input("Pilih fungsi:"))
    if p == 1:
        return tambah
    if p == 2:
        return kurang
    if p == 3:
        return kali
    if p == 4:
        return bagi
    return dummy_error

def main():
    c = 7
    d = 3
    # Test fungsi sebagai parameter
    hasil = prosesor(tambah, c, d)
    print("tambah: ", hasil)
    hasil = prosesor(kurang, c, d)
    print("kurang: ", hasil)
    hasil = prosesor(kali, c, d)
    print("kali: ", hasil)
    hasil = prosesor(bagi, c, d)
    print("bagi: ", hasil)

    # Komposisi fungsi 1
    e = 5
    hasil = prosesor(kali, prosesor(tambah, c, d), e)
    print("tambah kemudian kali: ", hasil)

    # Komposisi fungsi 2 - fungsi diproses di parameter
    hasil = prosesor(pilih_operasi(), c, d)
    print("hasil:", hasil)

    # Komposisi fungsi 3 - fungsi diproses di tempat tujuan
    hasil = prosesor2(pilih_operasi, c, d)
    print("hasil:", hasil)

    # Menambahkan kasus baru - komposisi fungsi dengan fungsi tambahan
    f = 2
    hasil = prosesor(kali, prosesor(tambah, c, d), prosesor(kurang, e, f))
    print("tambah kemudian kali dengan fungsi tambahan: ", hasil)

if __name__ == "__main__":
    main()
