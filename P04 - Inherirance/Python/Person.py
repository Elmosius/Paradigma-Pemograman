# Inherirance - parent class

class Person:
    def __init__(self):
        self.__nik: str = "12345"
        self.__name: str = "bcd"
        
    @property
    def nik(self) -> str:
        return self.__nik
    
    @nik.setter
    def nik(self, nik:str) -> None:
        self.__nik = nik
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name = name
        
    def __str__(self) -> str:
        return "NIK: " + self.nik + " | Nama: " + self.name
        
def main():
    p = Person()
    print(p)
    p.nik = "12345"
    p.name = "Person"
    print(p)
        
if __name__ == "__main__":
    main()