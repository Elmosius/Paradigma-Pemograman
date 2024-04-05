# Polymorphism
class Kucing:
    def __init__(self) -> None:
        self.jenis: str = "jenis kucing"
        
    def bersuara(self) -> str:
        self.jenis = "kucing"
        return self.jenis + " miauuwww..."
    
    