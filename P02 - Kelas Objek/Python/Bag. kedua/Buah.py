# File: Buah.py
# Penulis : Elmosius Suli
# Membuat kelas Buah

class Buah:
    def __init__(self, nama:str, warna:str, rasa:str, berat:int) -> None:
        self.nama = nama 
        self.warna = warna
        self.rasa = rasa
        self.berat = berat
        # kalau beratnya kurang dari 1 kg
        if (self.berat < 1):
            self.berat = 1
        return
    
    def hitung_harga(self) -> int :
        return (self.berat*5000)
    
    def tampilkan(self) -> None:
        print("Nama  : ", self.nama, "\nWarna : ", self.warna, "\nRasa  : ", self.rasa, "\nBerat : ", self.berat, "kg")
        print("Harga : ", self.hitung_harga(), '\n')
        return
    
## Program utama ##
def main():
    b1 = Buah("Semangka", "Hijau", "Manis", 3)
    b2 = Buah("Pisang", "Kuning", "Manis", 2)
    b3 = Buah("Jeruk", "Kuning", "Manis Asam", 0.2)

    print("Macam-macam Buah: \n")
    print("Buah 1. ")
    b1.tampilkan()
    
    print("Buah 2. ")
    b2.tampilkan()
    
    print("Buah 3. ")
    b3.tampilkan()

    print("="*40)

    harga = 0
    berat = 0
    pilih = int(input("Kode buah yang ingin dibeli (0 untuk selesai) : "))
    while (pilih != 0):
        if (pilih == 1):
            harga += b1.hitung_harga()
            berat += b1.berat
            print(f"Membeli {b1.nama} seberat {b1.berat} kg seharga Rp{b1.hitung_harga()},-")
        elif (pilih == 2):
            harga += b2.hitung_harga()
            berat += b2.berat
            print(f"Membeli {b2.nama} seberat {b2.berat} kg seharga Rp{b2.hitung_harga()},-")
        elif (pilih == 3):
            harga += b3.hitung_harga()
            berat += b3.berat
            print(f"Membeli {b3.nama} seberat {b3.berat} kg seharga Rp{b3.hitung_harga()},-")
        pilih = int(input("Kode buah yang ingin dibeli (0 untuk selesai) : "))

    print(f"Total berat = {berat} kg")
    print(f"Total belanjaan = Rp{harga},-")
    bayar = int(input("Uang yang dibayar: "))
    print(f"Kembaliannya Rp{bayar-harga},-")
  
if __name__ == '__main__':
    main()
  