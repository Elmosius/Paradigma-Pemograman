# Contoh raise exception
from typing import List

class EvenOnly(List[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Hanya bisa menambahkan bilangan bulat!")
        if value % 2 != 0:
            raise ValueError("Hanya bisa menambahkan bilangan genap!")
        super().append(value)
        
def main():
    # Keadaakn normal tidak raise exception
    print("Keadaan normal tidak raise exception:")
    my_list = EvenOnly()
    my_list.append(4)
    my_list.append(8)
    print("Isi list: " + my_list.__str__())
    
    # Coba exception tanpa try-except, coba buka baris yg di comment
    # secara bergantian, jalankan, dan lihat exception yg muncul
    print("\nCoba exception tanpa try-except:")
    # my_list.append(2.5)
    print("Isi list: " + my_list.__str__())
    # my_list.append(3)
    print("Isi list: " + my_list.__str__())
    
    # Coba exception yang sudah ditangani dengan try-except
    print("\nCoba exception dengan try-except:")
    try:
        my_list.append(2.5)
    except TypeError as te:
        print("Exception: " + te.__str__())
    print("Isi list: " + my_list.__str__())
    
    try:
        my_list.append(3)
    except TypeError as ve:
        print("Exception: " + ve.__str__())
    print("Isi list: " + my_list.__str__())
    
    
if __name__ == "__main__":
    main( )    