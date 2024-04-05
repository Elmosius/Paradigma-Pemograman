from Bidang2 import Bidang2
from Movement import Movement
# Bidang dan Movement kelas biasa

class Segi4b(Bidang2, Movement):
    # Pytrhon memperbolehkan mutiple inheritance
    
    def __init__(self):
        self.panjang: int = 12
        self.lebar : int = 10
        self._x: int = 40
        self._y : int = 30
        
        
    def hitungLuas(self):
        return self.panjang * self.lebar
    
    
    def getClassName(self):
        return Segi4b.__name__
    
    # def MoveLeft(self)
    #     super().moveLeft()
    # Tidak wajib implementasi, sudah ada di parent
    
    # getter
    @property
    def x(self):
        return self._x
    
    # setter
    @x.setter
    def x(self, x: int):
        self._x = x