# File: MesinCuci.py
# Penulis : Elmosius Suli
# Membuat kelas MesinCuci

class MesinCuci:
    def __init__(self, merk:str, tipe:str, kapasitas:int, beratCucian:float, modePencucian:str, airHangat:bool) -> None:
        self.merk = merk
        self.tipe = tipe if tipe in {"top loading", "front loading"} else "top loading"
        self.kapasitas = kapasitas
        self.beratCucian = beratCucian
        self.modePencucian = modePencucian if modePencucian in {"ringan", "sedang", "berat"} else "sedang"
        self.airHangat = airHangat
        if (airHangat == True):
            self.teksAir = "menggunakan air hangat"
        else:
            self.teksAir = "tidak menggunakan air hangat"
        return

    def mencuci(self) -> str:
        return f"Sedang mencuci {self.beratCucian} kg pakaian, mode {self.modePencucian}, {self.teksAir}"

    def membilas(self) -> str:
        return f"Sedang membilas {self.beratCucian} kg pakaian, mode {self.modePencucian}, {self.teksAir}"

    def mengeringkan(self) -> str:
        return f"Sedang mengeringkan {self.beratCucian} kg pakaian, mode {self.modePencucian}, {self.teksAir}"

    def toString(self) -> str:
        return f"Dilakukan oleh mesin cuci dengan merk {self.merk}, tipe {self.tipe}, dengan kapasitas {self.kapasitas} kg"

    def tampilkan(self) -> None:
        print(self.mencuci())
        print(self.membilas())
        print(self.mengeringkan())
        print(self.toString(), "\n")

    def langkahPencucian(self):
        if (self.beratCucian > self.kapasitas):
            jumlahBagian = self.beratCucian // self.kapasitas + 1
            sisaCucian = self.beratCucian % self.kapasitas
            for i in range (jumlahBagian):
                if (i != jumlahBagian - 1):
                    self.beratCucian = jumlahBagian
                else:
                    self.beratCucian = sisaCucian
                self.tampilkan()
        else:
            self.tampilkan()

## Program utama ##
def main():
    m1 = MesinCuci("Samsung", "front loading", 3, 8, "ringan", True)
    m2 = MesinCuci("LG", "back loading", 6, 2, "sangat berat", False)

    m1.langkahPencucian()
    m2.langkahPencucian()

if __name__ == '__main__':
    main()