from Kakek import Kakek

class Bapak(Kakek):
    def __init__(self) -> None:
        super().__init__()
        self._keterangan = "Bapak"
        print(self._keterangan)
        