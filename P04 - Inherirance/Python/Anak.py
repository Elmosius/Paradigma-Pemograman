from Bapak import Bapak

class Anak(Bapak):
    def __init__(self) -> None:
        super().__init__()
        self._keterangan = "Anak"
        print(self._keterangan)
        