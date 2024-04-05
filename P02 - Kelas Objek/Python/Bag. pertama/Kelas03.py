# File: Kelas03.py
# Penulis : Elmosius Suli
# Docstrings untuk menyisipkan dokumentasi langsung di dalam program

class Kelas03:
    """
    Kelas03 digunakan untuk menunjukkan docstrings.
    Jika docstrings lebih dari 1 baris, 
    maka bisa menggunakan 3 buah tanda kutip ganda
    atau tanda kutip tunggal, seperti ini.
    """
    pass
# Ini sudah diLuar KeLasO3

## Program utama ##
def main():
    "Ini docstrings di dalam main()"
    k = Kelas03()
    
# Perintah untuk menjaLankan method main() hanya jika keLas di run sendiri,
# bukan di import dari keLas Lain.

if __name__ == '__main__':
    main()
    help(Kelas03) # MenampiLkan docstrings
    help(main)