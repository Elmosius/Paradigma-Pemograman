# File: Tabungan.py
# Penulis : Elmosius Suli
# Membuat kelas Tabungan

class Tabungan:
    def __init__(self, namaBank:str, noRek:str, saldo:int, totalDebet:int, totalKredit:int) -> None:
        self.namaBank = namaBank
        self.noRek = noRek
        self.saldo = saldo
        self.totalDebet = totalDebet
        self.totalKredit = totalKredit
        return

    def cetakRek(self) -> None:
        print("-----------------------------")
        print("Informasi tabungan saat ini")
        print("-----------------------------")
        print("Nama Bank    :", self.namaBank)
        print("No Rekening  :", self.noRek)
        print("Saldo        :", self.saldo)
        print("Total Debet  :", self.totalDebet)
        print("Total Kredit :", self.totalKredit)
        print("-----------------------------")

    def menabung(self, rpDitabung:int) -> None:
        self.saldo += rpDitabung
        self.totalDebet += rpDitabung

    def mengambil(self, rpDiambil:int) -> None:
        self.saldo -= rpDiambil
        self.totalKredit += rpDiambil

    def tutupRek(self) -> None:
        self.namaBank = ""
        self.noRek = ""
        self.saldo = 0
        self.totalDebet = 0
        self.totalKredit = 0

## Program utama ##
def main():
    inputUser = input("Masukkan Username : ")
    inputPass = input("Masukkan Password : ")

    while (inputUser != "elmo123" or inputPass != "123456"):
        print("Username atau Password salah! Coba lagi")
        inputUser = input("Masukkan Username : ")
        inputPass = input("Masukkan Password : ")

    t1 = Tabungan("Bank ABC", "1234567890", 2000000, 1000000, 1000000)

    t1.cetakRek()

    print("Apa yang ingin dilakukan?")
    print("1. Menabung")
    print("2. Tarik Saldo")
    print("3. Tutup Rekening")
    print("0. Keluar")
    pilih = int(input("Silakan masukkan angka : "))

    while (pilih != 0):
        if (pilih == 1):
            rpDitabung = int(input("Jumlah yang ingin ditabung : "))
            t1.menabung(rpDitabung)
        elif (pilih == 2):
            rpDiambil = int(input("Jumlah yang ingin diambil : "))
            t1.mengambil(rpDiambil)
        elif (pilih == 3):
            t1.tutupRek()

        t1.cetakRek()

        print("Apa yang ingin dilakukan?")
        print("1. Menabung")
        print("2. Tarik Saldo")
        print("3. Tutup Rekening")
        print("0. Keluar")
        pilih = int(input("Silakan masukkan angka : "))

if __name__ == '__main__':
    main()