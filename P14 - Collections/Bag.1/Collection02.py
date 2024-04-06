# Fungsi any(), all(), len(), sum()

# Fungsi any dapat digunakan untuk mengecek apakah terdapat value yang bernilai 'True'
# pada sebuah list

# Sedangkan fungsi all mirip seperti fungsi any, namun dia hanya mengembalikan True jika semua valuenya bernilai 'True'
def main():
    
    # nilai = [80, 70, 90, 100]                               # contoh list berisikan nilai - nilai
    # cek = list(map(lambda x: x <= 75, nilai))               # map list untuk mengecek apakah ada yang kurang dari 75
    #                                                         # (akan menghasilkan list baru)
    # # print(cek)                                            @ uncomment jika ingin melihat hasil list dari mapnya
    # print("Apakah ada yang kurang dari 75?", any(cek))
    
    # print("Apakah semua nilai kurang dari 75?", all(cek))
    
    # # fungsi len akan mengembalikan panjang dari sebuah list
    # print("Jumlah data nilai: ", len(nilai))
    
    # # fungsi sum akan mengembalikan total dari sebuah list
    # print("Jumlah nilai: ", sum(nilai))
    
    
    # Mencoba kasus baru 
    nilai = list(map(int, input("Masukkan nilai-nilai siswa, dipisahkan oleh koma: ").split(',')))

    semua_lulus = all(x >= 75 for x in nilai)
    print("Apakah semua siswa lulus?", "Ya" if semua_lulus else "Tidak")

    ada_yang_tidak_lulus = any(x < 75 for x in nilai)
    print("Apakah ada siswa yang tidak lulus?", "Ya" if ada_yang_tidak_lulus else "Tidak")

    jumlah_siswa = len(nilai)
    print(f"Jumlah siswa: {jumlah_siswa} siswa")

    total_nilai = sum(nilai)
    print(f"Total nilai: {total_nilai} poin")

    rata_rata = total_nilai / jumlah_siswa if jumlah_siswa else 0
    print(f"Nilai rata-rata: {rata_rata:.2f} poin")
if __name__ == '__main__':
    main()