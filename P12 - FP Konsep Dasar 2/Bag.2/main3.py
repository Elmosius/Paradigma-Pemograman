from ContohEager import ContohEager
from ContohLazy import ContohLazy


class Main():
    def main():

# Penggunaan Lazy
        panggil_lazy = ContohLazy(5)
        lazy_generator = panggil_lazy.lazy_evaluation()

        # Evaluasi nilai hanya bila diperlukan sehingga dapat menunda perhitungan nilai hingga diperlukan
        print("Lazy Evaluation:")
        for hasil_lazy in lazy_generator:
            print(hasil_lazy, end=' ')

# Penggunaan Eager
        panggil_eager = ContohEager(5)
        hasil_eager = panggil_eager.eager_evaluation()

        # Evaluasi secara langsung
        # Evaluasi secara 'eager' dapat menghemat memori karena perhitungan hanya dilakukan ketika fungsi dipanggil
        print("\nEager Evaluation:")
        print(hasil_eager)

if __name__ == "__main__":
    Main.main()