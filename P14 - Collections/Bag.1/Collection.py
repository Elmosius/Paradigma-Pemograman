import random


def main():
    mahasiswa = ['Bernadus', 'Celine', 'Darren', 'Jessica', 'Grace']
    nilai_tugas1 = {
        'Bernadus': random.randint(40,100),
        'Celine': random.randint(40,100),
        'Darren': random.randint(40,100),
        'Jessica': random.randint(40,100),
        'Grace': random.randint(40,100)
    }

    nilai_tugas2 = {
        'Bernadus': random.randint(50,100),
        'Celine': random.randint(50,100),
        'Darren': random.randint(50,100),
        'Jessica': random.randint(50,100),
        'Grace': random.randint(50,100)
    }

    print("Mhasiswa:", mahasiswa)
    print("Nilai Tugas 1:", nilai_tugas1)
    print("Nilai Tugas 2:", nilai_tugas2)

    # mencari apakah ada nilai yang lebih dari 75 di kedua tugas
    nilai_diatas_kkm = ([nilai > 75 for nilai in nilai_tugas1.values()] + [nilai >=75 for nilai in nilai_tugas2.values()])
    ada_nilai_diatas_kkm = any(nilai_diatas_kkm)

    if ada_nilai_diatas_kkm:
        print("Ada nilai diatas KKM")
    else:
        print("Tidak ada nilai diatas KKM")

    # mencari apakah ada mahasiswa yang mendapatkan nilai 90 disalah satu nilai_tugas menggunakan method any()
    nilai_diatas_90 = [nilai >= 90 for nilai in nilai_tugas1.values()] + [nilai >= 90 for nilai in nilai_tugas2.values()]
    ada_nilai_diatas_90 = any(nilai_diatas_90)
    print("Apakah ada mahasiswa yang mendapatkan nilai diatas 90 ?", ada_nilai_diatas_90)

    # mencari apakah semua mahasiswa mendapat nilai 90 dari kedua tugas tersebut ? menggunakan method all()
    nilai_diatas_75 = [nilai >= 75 for nilai in nilai_tugas1.values()] + [nilai >= 75 for nilai in nilai_tugas2.values()]
    semua_nilai_diatas_90 = all(nilai_diatas_75)
    print("Apakah semua mahasiswa mendapatkan nilai diatas 90 ?", semua_nilai_diatas_90)

    # membuat rekapan nilai mahasiswa menggunakan method zip()
    data_nilai_mahasiswa = list(zip(mahasiswa, nilai_tugas1.values(), nilai_tugas2.values()))
    print("Data Mahasiswa:")
    for data in data_nilai_mahasiswa:
        print(data)
    
    # mencari rata - rata nilai tugas
    rata_rata_nilai = {nama: (nilai_tugas1[nama] + nilai_tugas2[nama]) / 2 for nama in mahasiswa}
    for nama, rata_rata in rata_rata_nilai.items():
        print(f"Nilai rata-rata {nama}:", rata_rata)


    # menampilkan informasi statistik
    jumlah_mahasiswa = len(mahasiswa)
    total_nilai_tugas1 = sum(nilai_tugas1.values())
    total_nilai_tugas2 = sum(nilai_tugas2.values())

    print("Informasi Statistik:")
    print(f"Jumlah mahasiswa: {jumlah_mahasiswa}")
    print(f"Total nilai tugas 1: {total_nilai_tugas1}")
    print(f"Total nilai tugas 2: {total_nilai_tugas2}")

    # mengurutkan siswa berdasarkan nilai rata-rata
    urutkan_mahasiswa = sorted(data_nilai_mahasiswa, key= lambda x: rata_rata_nilai[x[0]], reverse=True)
    print("Mahasiswa berdasarkan nilai rata-rata:")
    for data in urutkan_mahasiswa:
        print(data)

if __name__ == "__main__":
    main()