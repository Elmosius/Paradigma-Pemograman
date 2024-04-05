from Bidang import Bidang

class Segi3(Bidang):
    def __init__(self):
        self.alas : int = 20
        self.tinggi : int = 17
                
    def hitungLuas(self):
        return self.alas * self.tinggi / 2
    # Coba ubah jadi komentar method hitungLuas()
    
    def getClassName(self):
        return "Segi3"
    
def main():
    s3 = Segi3()
    # Tidak error karena membuat method hitungLuas()
    print("Luas ", s3.getClassName(), ":", s3.hitungLuas())
    
if __name__ == '__main__':
    main()