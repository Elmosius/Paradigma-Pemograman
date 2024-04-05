from Segi4 import Segi4

class Kubus(Segi4):
    def __init__(self)-> None:
        self.sisi: int = 5
        
    def hitungLuas(self):
        return self.sisi * self.sisi * 6
    
    def getClassName(self):
        return Kubus.__name__
    
def main():
    k = Kubus()
    # Tidak error karena membuat method hitungLuas()
    print("Luas ", k.getClassName(), ":", k.hitungLuas())
    
if __name__ == '__main__':
    main()