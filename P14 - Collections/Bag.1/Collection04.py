# Fungsi enumerate
# Fungsi enumerate dapat digunakan untuk mendapatkan tuple yang berisikan indeks dan data dari sebuah Iterable
# Iterable bisa berupa list, tuple, string, dan set

def main():
    # contoh enumerate pada sebuah list
    nama = ["Paula", "Valerya", "Dorothy", "Moses", "Marzuki", "Samosir"]
    print(list(enumerate(nama)))
    
    # contoh enumerate pada sebuah string
    n2= "Lola"
    print(list(enumerate(n2)))

    # # Bikin studi kasus menggunakan enumerate
    # buku = input("Masukkan nama-nama buku, dipisahkan oleh koma: ").split(',')

    # for i, b in enumerate(buku, start=1):
    #     print(f"Buku ke-{i}: {b.strip()}")

    
if __name__ == '__main__':
    main()