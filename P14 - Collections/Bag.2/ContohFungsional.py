# Contoh penerapan generator dan iter untuk functional programming
from random import randint

# membuat generator x angka random
def myGenerator(x: int):
    for i in range(x):
        yield randint(1,10)
        
# fungsi untuk mencari jumlah dari angka secara rekursif
def sum(angka):
    try:
        currentNum = next(angka)
        print(str(currentNum), "+ ", end="")
        return currentNum + sum(angka)
    except StopIteration:  # StopIteration akan terjadi saat iterator sudah habis
        print("0 = ")
        return 0
    
def main():
    # buat data pada sebuah list
    angka = [1,2,3,4,5]
    print(sum(iter(angka)))
    
    print("\nHasil sum random:")
    # coba mencari sum dari 5 angka random
    print(sum(myGenerator(5)))
    
if __name__ == '__main__':
    main()