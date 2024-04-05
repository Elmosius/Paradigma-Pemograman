class Kendaraan:
    # atribut yang merupakan class member,
    # hanya ada 1, di share oleh semua objek
    jml_kendaraan: int = 0
    
    
    def __init__(self) -> None:
        self._kecepatan_maks: int= 0
        self._kapasistas_penumpang: int = 0
        Kendaraan.jml_kendaraan += 1
        
        
    