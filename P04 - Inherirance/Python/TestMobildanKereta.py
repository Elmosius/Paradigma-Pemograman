# File TestMobildanKereta.py

from Kendaraan import Kendaraan
from Mobil import Mobil
from Kereta import Kereta

def main():
    sedan = Mobil()
    print("Sedanku:")
    print("Kecepatan Maks: " + str(sedan._kecepatan_maks)) 
    print("Kapasitas Penumpang: " + str(sedan._kapasistas_penumpang))
    print("Bahan Bakar: " + sedan.bahan_bakar)
    print("Jenis Mesin: " + sedan.mesin)
    print("Jumlah kendaraan: " + str(Kendaraan.jml_kendaraan))
    
    andong = Kereta()
    print("\nAndongku:")
    print("Kecepatan Maks: " + str(andong._kecepatan_maks)) 
    print("Kapasitas Penumpang: " + str(andong._kapasistas_penumpang))
    print("Tenaga Penarik: " + andong.tenaga_penarik)
    print("Jumlah Penarik: " + str(andong.jml_penarik))
    print("Jumlah kendaraan: " + str(Kendaraan.jml_kendaraan))
    
if __name__ == "__main__":
    main()