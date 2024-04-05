# File: Waktu.py
# Penulis : Elmosius Suli
# Membuat kelas Waktu

class Waktu:
    def __init__(self, jam:int, menit:int, detik:int) -> None:
        self.jam = jam
        self.menit = menit
        self.detik = detik
        return

    def toString(self) -> None:
        print("Jam   :", self.jam)
        print("Menit :", self.menit)
        print("Detik :", self.detik)
        print("Jam Saat Ini : ", end="")
        self.tampilkan_jam()
        print("Jumlah Detik :", self.waktu_to_detik(), '\n')

    def tampilkan_jam(self) -> None:
        print(f"{self.jam:02d}:{self.menit:02d}:{self.detik:02d}")

    def waktu_to_detik(self) -> int:
        return self.jam * 3600 + self.menit * 60 + self.detik

    def detik_to_waktu(self, jml_detik:int) -> None:
        print("Jika jumlah detik diubah menjadi", jml_detik)
        print("Datanya akan menjadi seperti ini")
        self.jam = jml_detik // 3600
        self.sisa_detik = jml_detik % 3600
        self.menit = self.sisa_detik // 60
        self.detik = self.sisa_detik % 60
        self.toString()

    def tambahWaktu(self, jamTambah:int, menitTambah:int, detikTambah:int) -> None:
        jumlahDetik = self.detik + detikTambah
        menitTambahan = jumlahDetik // 60
        self.detik = jumlahDetik % 60

        jumlahMenit = self.menit + menitTambah + menitTambahan
        jamTambahan = jumlahMenit // 60
        self.menit = jumlahMenit % 60

        self.jam = self.jam + jamTambah + jamTambahan

    def kurangiWaktu(self, jamKurang:int, menitKurang:int, detikKurang:int) -> None:
        if self.detik < detikKurang:
            self.detik += 60
            self.menit -= 1
        
        self.detik = self.detik - detikKurang
        
        if self.menit < menitKurang:
            self.menit += 60
            self.jam -= 1
        
        self.menit = self.menit - menitKurang
        self.jam = self.jam - jamKurang

## Program utama ##
def main():
    w1 = Waktu(2, 3, 4)
    w2 = Waktu(12, 12, 12)
    w3 = Waktu(1, 6, 40)

    w1.toString()
    w2.toString()
    w3.toString()

    w3.detik_to_waktu(5000)

    print("1. Tambahkan Waktu")
    print("2. Kurangi Waktu")
    print("0. Keluar")
    pilih = int(input("Masukkan kode yang ingin dilakukan : "))

    while (pilih != 0):
        if (pilih == 1):
            jamT = int(input("Jam yang ingin ditambah: "))
            menitT = int(input("Menit yang ingin ditambah: "))
            detikT = int(input("Detik yang ingin ditambah: "))
            w3.tambahWaktu(jamT, menitT, detikT)
        elif (pilih == 2):
            jamK = int(input("Jam yang ingin dikurang: "))
            menitK = int(input("Menit yang ingin dikurang: "))
            detikK = int(input("Detik yang ingin dikurang: "))
            w3.kurangiWaktu(jamK, menitK, detikK)
        w3.toString()
        print("="*40)
        print("1. Tambahkan Waktu")
        print("2. Kurangi Waktu")
        print("0. Keluar")
        pilih = int(input("Masukkan kode yang ingin dilakukan : "))

if __name__ == '__main__':
    main()