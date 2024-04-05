# File: Kelas02.py
# Penulis : Elmosius Suli
# Method main() untuk menjalankan program

# pass untuk menunjukkan keLas kosong 
class Kelas02:
    # pass untuk menunjukkan keLas kosong 
    pass

# Int sudah diLuar KeLas02

## Program utama ##
def main():
    k = Kelas02()   # membuat objek k yang spesifikasinya sesuat KeLas2
    print(k)        # print objek k
    print(type(k))  # mengecek tipe data
 
# Perintah untuk menjaLankan method main() hanya jika keLas di run sendiri,
# bukan di import dari keLas Lain.
if __name__ == '__main__':
    main() # panggil method main()