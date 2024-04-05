# File: JadwalKuliah.py
# Penulis : Elmosius Suli
# Membuat kelas JadwalKuliah

class JadwalKuliah:
    def __init__(self, mataKuliah:str, hari:str, waktu:str, ruang:str, jmlSks:int) -> None:
        self.mataKuliah = mataKuliah
        self.hari = hari
        self.waktu = waktu
        self.ruang = ruang
        self.jmlSks = jmlSks
        return

    def durasi(self) -> int:
        return self.jmlSks * 50

    def toString(self) -> str:
        return f"Durasi belajar = {self.durasi()} menit"

    def tampilkan(self) -> None:
        print("Mata Kuliah :", self.mataKuliah)
        print("Hari        :", self.hari)
        print("Waktu       :", self.waktu)
        print("Ruang       :", self.ruang)
        print("Jumlah SKS  :", self.jmlSks)

## Program utama ##
def main():
    urutan_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

    j1 = JadwalKuliah("Paradigma Pemrograman", "Rabu", "09:30", "Adv 3", 4)
    j2 = JadwalKuliah("Matematika Diskrit", "Senin", "07:00", "Adv 2", 3)
    j3 = JadwalKuliah("Teknologi Multimedia", "Selasa", "07:30", "Adv 1", 2)

    jadwal_kuliah = [j1, j2, j3]

    jadwal_kuliah.sort(key=lambda x: urutan_hari.index(x.hari))

    for jadwal in jadwal_kuliah:
        jadwal.tampilkan()
        print(jadwal.toString(), "\n")

if __name__ == '__main__':
    main()