# Paradigma dengan pendekatan imperatif berfokus pada proses / langkah-langkah tentang cara melakukan tugas yang dikerjakan
class ContohImperatif:
    def jumlah_kaudrat_bilangan_ganjil(self, batas):
        angka = list(range(batas))      # membuat list angka dengan batasan yang ditentukan
        total = 0                       # membuat variabel penampung

        for num in angka:               # melakukan perulangan
            if num % 2 != 0:            # mencari bilangan ganjil
                total += num**2         # menjumlahkan kuadrat
        
        return total