# Fungsi sorted(), dan reversed()

def main():
    nama = ["Paula", "Valerya", "Dorothy", "Moses", "Marzuki", "Samosir"]
    
    # fungsi sorted dapat digunakan untuk sorting data pada sebuah list
    # jika tipe data adalah str maka yang disortir adalah huruf pertama dari setiap string (A-Z)
    
    print("Sorted: ", sorted(nama))
    
    # fungsi reversed dapat digunakan untuk membalikan urutan data pada sebuah list
    print("\nAsli: ", nama)
    print("Reversed: ", list(reversed(nama)))
    
    
    # # Membuat kasuss baru kurang lebih kaya sebelumnya namun memakai fungsi sorted() dan reversed():
    # nama = input("Masukkan nama-nama siswa, dipisahkan oleh koma: ").split(',')

    # sorted_nama = sorted(nama)
    # print("Daftar siswa dalam urutan alfabet: ", ', '.join(sorted_nama))
    
    # reversed_nama = list(reversed(sorted_nama))
    # print("Daftar siswa dalam urutan terbalik: ", ', '.join(reversed_nama))
    
    # jumlah_siswa = len(nama)
    # print(f"Jumlah siswa: {jumlah_siswa} siswa")
    
if __name__ == '__main__':
    main()