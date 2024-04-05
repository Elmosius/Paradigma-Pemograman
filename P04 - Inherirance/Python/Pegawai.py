class Pegawai:
    def __init__(self, nama:str, gaji: int) -> None:
        self.__nama: str = nama
        self.__gaji: int = gaji
        
    @property
    def nama(self) -> str:
        return self.__nama
    
    
    @property
    def gaji(self) -> int:
        return self.__gaji
    
    