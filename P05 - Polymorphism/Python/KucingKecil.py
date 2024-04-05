from Kucing import Kucing

class KucingKecil(Kucing):
    def bersuara(self):
        self.jenis = "kucing kecil"
        return self.jenis + "miau...miaw...miaw..."
    
    