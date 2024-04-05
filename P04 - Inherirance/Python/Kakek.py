from Buyut import Buyut

class Kakek(Buyut):
    def __init__(self) -> None:
        super().__init__()
        self._keterangan = "Kakek"
        print(self._keterangan)
        