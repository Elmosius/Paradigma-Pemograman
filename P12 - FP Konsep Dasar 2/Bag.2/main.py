# import modul
from ContohDeklaratif import ContohDeklaratif
from ContohImperatif import ContohImperatif


class Main:
    @staticmethod
    def main():
        # Penggunaan untuk pendekatan imperatif
        panggil_imperatif = ContohImperatif()                           # membuat objek
        imperatif = panggil_imperatif.jumlah_kaudrat_bilangan_ganjil(7) # menghitung
        print("Imperatif:", imperatif)                                  # menampilkan 

        # Penggunaan untuk pendekatan deklaratif
        panggil_deklaratif = ContohDeklaratif()                             # membuat objek Deklaratif
        deklaratif = panggil_deklaratif.jumlah_kaudrat_bilangan_ganjil(7)   # menghitung
        print("Deklaratif:", deklaratif)                                    # menampilkan

if __name__ == "__main__":
    Main.main()