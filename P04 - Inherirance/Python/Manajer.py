from Pegawai import Pegawai

class Manajer(Pegawai):
    def __init__(self, namanya: str, gajinya: int) -> None:
        super().__init__(namanya, gajinya)
        self.__bonus: int =0
        
        
    @property
    def bonus(self) -> int:
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonusnya: int) -> None:
        self.__bonus = bonusnya
        
    @property
    def gaji(self)-> int:
        gaji_pokok = super().gaji
        return gaji_pokok + self.bonus