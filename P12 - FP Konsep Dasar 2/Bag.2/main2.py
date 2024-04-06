# import modul
from ContohMutable import ContohMutable
from ContohImmutable import ContohImmutable

class Main:
    def main():
        panggil_imutable = ContohImmutable([1, 2, 3])                           # panggil immutable
        print("Nilai Immutable:", panggil_imutable.get_values())                # mencetak nilai immutable
        # Akan menghasilkan error karena mencoba mengubah nilai di dalam tuple
        # panggil_immutable.change_value(4)
        # print("Nilai Immutable:", panggil_immutable.get_values())

        panggil_mutable = ContohMutable([1, 2, 3])                          # panggil mutable
        print("Nilai Mutable:", panggil_mutable.get_values())               # mencetak nilai mutable
        panggil_mutable.change_value(4)                                     # mengubah nilai mutable
        print("Nilai Mutable:", panggil_mutable.get_values())               # mencetak nilai mutable yang sudah diubah

if __name__ == "__main__":
    Main.main()