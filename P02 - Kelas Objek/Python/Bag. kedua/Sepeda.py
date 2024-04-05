# File: Sepeda.py
# Penulis : Elmosius Suli
# Membuat kelas Sepeda

class Sepeda:
    def __init__(self, merk: str, tipe: str, gigi_sekarang: int, kecepatan: int) -> None:
        self.merk = merk
        self.tipe = tipe
        self.gigi_sekarang = gigi_sekarang
        self.kecepatan = kecepatan
        return

    def setMerk(self, merk: str) -> None:
        self.merk = merk

    def setTipe(self, tipe: str) -> None:
        self.tipe = tipe

    def naikkanGigi(self) -> None:
        self.gigi_sekarang += 1

    def turunkanGigi(self) -> None:
        self.gigi_sekarang -= 1

    def tambahKecepatan(self, tambah: int) -> None:
        self.kecepatan += tambah

    def rem(self, kurangi: int) -> None:
        self.kecepatan -= kurangi

    def cetakKondisi(self) -> None:
        print("--------------------------------------------------")
        print(
            f"Kamu sedang mengendarai sepeda merk {self.merk} dengan tipe {self.tipe}")
        print(
            f"Sepeda melaju dengan kecepatan {self.kecepatan} km/jam menggunakan gigi {self.gigi_sekarang}")

## Program utama ##
def main():
    s1 = Sepeda("Giant", "sepeda lipat", 1, 15)

    s1.cetakKondisi()
    print("Apa yang ingin kamu lakukan sekarang?")
    print("1. Mengganti sepeda")
    print("2. Menaikkan gigi")
    print("3. Menurunkan gigi")
    print("4. Menambah kecepatan")
    print("5. Rem")
    print("0. Berhenti")
    pilih = int(input("Silakan masukkan angka : "))

    while (pilih != 0):
        if (pilih == 1):
            merkBaru = input(
                "Merk Sepeda Baru (isikan '-' jika merk tidak berubah) : ")
            tipeBaru = input("Tipe Sepeda Baru : ")
            if (merkBaru != "-"):
                s1.setMerk(merkBaru)
            s1.setTipe()
        elif (pilih == 2):
            s1.naikkanGigi()
        elif (pilih == 3):
            s1.turunkanGigi()
        elif (pilih == 4):
            tambah = int(input("Berapa kecepatan yang ditambah? "))
            s1.tambahKecepatan(tambah)
        elif (pilih == 5):
            kurangi = int(input("Berapa kecepatan yang dikurangi? "))
            s1.rem(kurangi)

        if (s1.kecepatan != 0):
            s1.cetakKondisi()
            print("Apa yang ingin kamu lakukan sekarang?")
            print("1. Mengganti sepeda")
            print("2. Menaikkan gigi")
            print("3. Menurunkan gigi")
            print("4. Menambah kecepatan")
            print("5. Rem")
            print("0. Berhenti")
            pilih = int(input("Silakan masukkan angka : "))

    print("Sepeda kamu telah berhenti")

if __name__ == '__main__':
    main()
