# Higher-order function

# Fungsi untuk mencari nilai maksimum dengan fungsi kunci
def find_max(data, key_func):
    return max(data, key=key_func)

# Mendefinisikan fungsi kunci
def get_year(yc):
    return yc[0]  # Fungsi kunci untuk mendapatkan tahun

def get_cheese_amount(yc):
    return yc[1]  # Fungsi kunci untuk mendapatkan jumlah keju

def main():
    # Data tahun dan jumlah keju
    year_cheese = [
        (2000, 29.87), (2001, 30.12), (2002, 30.6),
        (2003, 30.66), (2004, 31.33), (2005, 32.62),
        (2006, 32.73), (2007, 33.5), (2008, 32.84),
        (2009, 33.02), (2010, 32.92)
    ]
    # Mencari tahun dengan nilai maksimum
    max_year = find_max(year_cheese, get_year)
    print("Tahun dengan jumlah keju maksimum:", max_year[0])

    # Mencari jumlah keju dengan nilai maksimum
    max_cheese_amount = find_max(year_cheese, get_cheese_amount)
    print("Jumlah keju maksimum:", max_cheese_amount[1])

    # Menggunakan higher-order function untuk mencari nilai maksimum berdasarkan jumlah keju
    max_by_cheese_amount = find_max(year_cheese, get_cheese_amount)
    print("Maksimum berdasarkan jumlah keju:", max_by_cheese_amount)

    # Menggunakan map dan fungsi unwrap untuk mencari nilai maksimum
    def unwrap(wrapped_data):
        return wrapped_data[1]

    max_unwrapped = find_max(map(lambda yc: (yc[1], yc), year_cheese), unwrap)
    print("Maksimum setelah di-unwrap:", max_unwrapped[1])


if __name__ == "__main__":
    main()
