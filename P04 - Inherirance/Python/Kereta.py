from Kendaraan import Kendaraan

class Kereta(Kendaraan):
    def __init__(self) -> None:
        super().__init__()
        self.tenaga_penarik: str = "Kuda"
        self.jml_penarik: int = 2
        self._kecepatan_maks = 50
        self._kapasistas_penumpang = 8
        
        