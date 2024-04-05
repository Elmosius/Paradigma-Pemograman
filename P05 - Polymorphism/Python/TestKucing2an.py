# Kelas untuk test
from Kucing import Kucing
from Harimau import Harimau
from KucingBesar import KucingBesar
from KucingDijual import KucingDijual
from KucingKecil import KucingKecil

def main():
    k1 = Kucing()
    k2 = KucingKecil()
    k3 = KucingBesar()
    k4 = Harimau()
    
    print("Beginilah kalau kucing2 bersuara bersamaan : ")
    print(k1.bersuara())
    print(k2.bersuara())
    print(k3.bersuara())
    print(k4.bersuara())
    
    print('\nList standar di Python memang bisa diisi objek2 yg berbeda: ')
    list_k = [k1,k2,k3,k4]
    for c in list_k:
        print(c.bersuara())
        
    j = KucingDijual()
    print("\nParameter di Python memang bisa terima objek2 yg berbeda")
    print("Jenis: " + j.cek_jenis(k1) + ", umur : " + str(j.cek_umur(k1)) + ", harga : " + str(j.cek_harga(k1)))
    print("Jenis: " + j.cek_jenis(k2) + ", umur : " + str(j.cek_umur(k2)) + ", harga : " + str(j.cek_harga(k2)))
    print("Jenis: " + j.cek_jenis(k3) + ", umur : " + str(j.cek_umur(k3)) + ", harga : " + str(j.cek_harga(k3)))
    print("Jenis: " + j.cek_jenis(k4) + ", umur : " + str(j.cek_umur(k4)) + ", harga : " + str(j.cek_harga(k4)))
    print("Jenis: " + j.cek_jenis(j) + ", umur : " + str(j.cek_umur(j)) + ", harga : " + str(j.cek_harga(j)))

if __name__ == "__main__":
    main()