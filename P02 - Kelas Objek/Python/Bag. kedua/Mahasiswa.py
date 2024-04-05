# File: Mahasiswa.py
# Penulis : Elmosius Suli
# Membuat kelas Mahasiswa

class Mahasiswa:
    def __init__(self, nama:str, nrp:str, kelas:str, nilai_KAT:int, nilai_UTS:int, nilai_UAS:int) -> None:
        self.nama = nama
        self.nrp = nrp
        self.kelas = kelas
        self.nilai_KAT = nilai_KAT
        self.nilai_UTS = nilai_UTS
        self.nilai_UAS = nilai_UAS
        return
    
    def hitung_nilai_akhir(self) -> float :
        self.nilai_akhir = (0.25*self.nilai_UTS) + (0.25*self.nilai_UAS) + (0.5*self.nilai_KAT)
        return self.nilai_akhir
    
    def predikat(self) -> str:
        if(self.nilai_akhir >= 80):
            self.predikat = ("A, Luar biasa")
        elif(self.nilai_akhir >= 75):
            self.predikat = ("B+, Sangat Baik")
        elif(self.nilai_akhir >= 70):
            self.predikat = ("B, Baik")
        elif(self.nilai_akhir >= 65):
            self.predikat = ("C+, Cukup Baik")
        elif(self.nilai_akhir >= 60):
            self.predikat = ("C,Cukup")
        elif(self.nilai_akhir >= 55):
            self.predikat = ("D, Kurang")
        else:
            self.predikat = ("D, Sangat Kurang")
        return self.predikat
    
    
    def toString(self) -> None:
        print("Nama        : ", self.nama)
        print("NRP         : ", self.nrp)
        print("Kelas       : ", self.kelas)
        print("KAT         : ", self.nilai_KAT)
        print("UTS         : ", self.nilai_UTS)
        print("UAS         : ", self.nilai_UAS)
        print("Nilai Akhir : ", self.hitung_nilai_akhir())
        print("Predikat    : ", self.predikat(), '\n')
        return
    
## Program utama ##
def main():
    m1 = Mahasiswa("Elmo", "2272008", "A", 100, 100, 100)
    m2 = Mahasiswa("Emily", "2272009", "B", 50, 80, 100)
    m3 = Mahasiswa("Grace", "2272028", "C", 80, 80, 80)
    
    print("Mahasiswa Teknologi Informasi Maranatha: \n")
    print("Mahasiswa 1.")
    m1.toString()
    
    print("Mahasiswa 2.")
    m2.toString()
    
    
    print("Mahasiswa 3.")
    m3.toString()
    
    
if __name__ == '__main__':
    main()
  