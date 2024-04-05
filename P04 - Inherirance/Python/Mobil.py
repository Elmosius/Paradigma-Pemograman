from Kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self) -> None:
        super().__init__()
        self.bahan_bakar: str = "Bensin"
        self.mesin: str = "EFI"
        self._kecepatan_maks= 100
        self._kapasistas_penumpang = 4