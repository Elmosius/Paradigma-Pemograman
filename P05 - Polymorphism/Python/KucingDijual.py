from Kucing import Kucing
from Harimau import Harimau
from KucingBesar import KucingBesar
from KucingKecil import KucingKecil

class KucingDijual:
    def cek_umur(self, miau: Kucing) -> int:
        return 3
    
    def cek_jenis(self, miau: Kucing) -> str:
        jns = ""
        if isinstance(miau, Harimau):
            jns = "harimau"
        elif isinstance(miau, KucingBesar):
            jns = "kucing besar"
        elif isinstance(miau, KucingKecil):
            jns = "kucing kecil"
        elif isinstance(miau, Kucing):
            jns = "kucing"
        return jns
    
    def cek_harga(self, miau: Kucing):
        harga = 0
        
        if isinstance(miau, Harimau):
            harga = 90000
        elif isinstance(miau, KucingBesar):
            harga = 50000
        elif isinstance(miau, KucingKecil):
            harga = 20000
        elif isinstance(miau, Kucing):
            harga = 15000
        return harga
        
        