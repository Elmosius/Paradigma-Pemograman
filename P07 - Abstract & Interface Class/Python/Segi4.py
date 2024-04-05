from Bidang import Bidang

class Segi4(Bidang):
    def __init__(self):
        self.panjang : int = 12
        self.lebar: int = 10
        
    def hitungLuas(self):
        return self.panjang * self.lebar
    # Coba ubah jadi komentar method hitungLuas()
    
    def getClassName(self):
        return "Segi4"
    
def main():
    d = Segi4()
    # Tidak error karena membuat method hitungLuas()
    print("Luas ", d.getClassName(), ":", d.hitungLuas())
    
if __name__ == '__main__':
    main()