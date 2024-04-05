# File AnekaBidangDatar

class Persegi:
    def __init__(self) -> None:
        self._panj_sisi: int = 0
        self._luas: int = 0
        
    @property
    def panj_sisi(self)-> int:
        return self._panj_sisi
    
    @panj_sisi.setter
    def panj_sisi(self, n:int) -> None:
        self._panj_sisi = n
        
    @property
    def luas(self) -> int:
        return self._luas
    
    def hitung_luas(self) -> int:
        self._luas = self._panj_sisi * self._panj_sisi
        
class PersegiPanjang(Persegi):
    def __init__(self) -> None:
        self.__lebar: int = 0
        
    @property
    def lebar_sisi(self) -> int:
        return self.__lebar_sisi
    
    @lebar_sisi.setter
    def lebar_sisi(self, n:int) -> None:
        self.__lebar_sisi = n
        
    def hitung_luas(self) -> int:
        self._luas = self.panj_sisi * self.__lebar_sisi
        
def main():
    p = Persegi()
    p.panj_sisi = 5
    p.hitung_luas()
    print("Bujur Sangkar:")
    print("Panj Sisi: " + str(p.panj_sisi))
    print("Luas: " + str(p.luas))
    print()
    
    pp = PersegiPanjang()
    pp.panj_sisi = 8
    pp.lebar_sisi = 4
    pp.hitung_luas()
    print("Persegi Panjang:")
    print("Panj Sisi: " + str(pp.panj_sisi))
    print("Lebar Sisi: " + str(pp.lebar_sisi))
    print("Luas: " + str(pp.luas))
    
if __name__ == "__main__":
    main()