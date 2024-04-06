# Paradigma dengan pendekatan deklaratif berfokus pada mendeskripsikan tugas yang dilakukan
class ContohDeklaratif:
    def jumlah_kaudrat_bilangan_ganjil(self, batas):
        angka = list(range(batas))                                  # membuat list angka dengan batasan yang ditentukan
        angka_ganjil = filter(lambda x: x % 2 != 0, angka)          # mengambil bilangan ganjil
        kuadrat_angka_ganjil = map(lambda x: x**2, angka_ganjil)    # menghitung kuadrat
        total = sum(kuadrat_angka_ganjil)                           # menjumlahkan

        return total