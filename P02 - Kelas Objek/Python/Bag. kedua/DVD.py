# File: DVD.py
# Penulis : Elmosius Suli
# Membuat kelas DVD

class DVD:
    def __init__(self, judul:str, jenis:str, harga:int, jumlahStock:int) -> None:
        self.judul = judul
        self.jenis = jenis if jenis in {"film", "musik", "game"} else "film"
        self.harga = harga
        self.jumlahStock = jumlahStock
        return

    def tampilkan(self) -> None:
        print("="*40)
        print("Judul        :", self.judul)
        print("Jenis        :", self.jenis)
        print("Harga        :", self.harga)
        print("Jumlah Stock :", self.jumlahStock)
        print(self.toString())

    def tambahStock(self, jumlah:int) -> int:
        self.jumlahStock += jumlah
        return self.jumlahStock

    def penjualan(self, jmlJual:int) -> float:
        self.jumlahStock -= jmlJual
        return self.harga * jmlJual

    def nilaiStock(self) -> float:
        self.nilaiStock = self.harga * self.jumlahStock
        return self.nilaiStock

    def toString(self) -> str:
        return f"Nilai stock dari DVD ini adalah sebesar Rp{self.nilaiStock()},-" 

## Program utama ##
def main():
    d1 = DVD("Paddle Pop Begins", "movie", 10000, 12)
    d1.tampilkan()
    d2 = DVD("The Sims", "game", 15000, 5)
    d2.tampilkan()
    print("="*40)

    status = int(input("Kamu adalah (1. Penjual, 2. Pembeli) : "))

    if (status == 1):
        print("Apa yang ingin dilakukan?")
        print("1. Menambah stock DVD")
        print("2. Menjual DVD")
        print("0. Keluar")
        pilih = int(input("Silakan masukkan angka : "))

        while (pilih != 0):
            if (pilih == 1):
                ditambah = int(input("Berapa stock yang ditambah? "))
                print(f"Stock DVD saat ini adalah {d1.tambahStock(ditambah)} buah")
            elif (pilih == 2):
                terjual = int(input("Berapa stock yang terjual? "))
                print(f"Terjual DVD {terjual} buah dengan harga Rp{d1.penjualan(terjual)},-")

            print("--------------------------")
            print("Apa yang ingin dilakukan?")
            print("1. Menambah stock DVD")
            print("2. Menjual DVD")
            print("0. Keluar")
            pilih = int(input("Silakan masukkan angka : "))
    
    elif (status == 2):
        harga = 0
        jml1 = 0
        jml2 = 0

        print(f"1. {d1.judul}")
        print(f"2. {d2.judul}")
        print("0. Keluar")
        pilihDVD = int(input("Masukkan kode DVD yang ingin dibeli: "))
        while (pilihDVD != 0):
            jumlah = int(input("Berapa banyak yang akan dibeli? "))
            if (pilihDVD == 1):
                harga += d1.harga * jumlah
                jml1 += jumlah
            elif (pilihDVD == 2):
                harga += d2.harga * jumlah
                jml2 += jumlah

            print(f"1. {d1.judul}")
            print(f"2. {d2.judul}")
            print("0. Keluar")
            pilihDVD = int(input("Masukkan kode DVD yang ingin dibeli: "))      

        print("Daftar DVD yang dibeli :")
        if (jml1 != 0):
            print(f"{d1.judul} sebanyak {jml1} buah")
        if (jml2 != 0):
            print(f"{d2.judul} sebanyak {jml2} buah")
        print(f"Total harga yang harus dibayar = Rp{harga},-")

if __name__ == '__main__':
    main()