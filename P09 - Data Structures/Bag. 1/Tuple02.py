# Belajar Tuples
import datetime

def middle(stock, date):
    # Unpack tuple stock menjadi ke-4 komponen-nya
    symbol, current, high, low = stock
    # Cek komponen hasil unpack
    print("Symbol: ", symbol, ", current: ", current, " high: ", high, ", low: ", low)
    
    # Tuple bisa digunakan dalam return
    return ((high + low ) /2, date)

def main():
    stock1 = ("APPL", 123.52, 137.98, 53.15)
    print("stock1: ", stock1)
    hasil = middle(stock1, datetime.date(2023, 11, 22))
    print("Hasil memanggil fungsi middle: ", hasil)
    
if __name__ == "__main__":
    main()