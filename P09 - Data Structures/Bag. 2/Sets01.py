# Set koleksi yang elemennya unik tidak ada duplikat dan tidak terurut

def main():
    kosong = set()
    print("kosong:", kosong)
    kosong.add("isi1")
    print("kosong:", kosong)

    basket = {"apel", "jeruk", "pisang", "nangka", "jeruk", "apel"}
    # jika dijalankan berulang2, urutan bisa berbeda2
    print("basket:", basket)
    print("ada jeruk?", "jeruk" in basket)
    print("ada melon?", "melon" in basket)

    m = set("maranatha")
    n = set("maret")
    print("m    : ", m)
    print("n    : ", n)
    print("m | n: ", m | n) # or
    print("m & n: ", m & n) # and
    print("m ^ n: ", m ^ n) # xor
    print("m - n: ", m - n)
    print("n - m: ", n - m)

    # set comprehension
    a = {x for x in "maranatha" if x not in "mar"}
    print("a: ", a)

if __name__ == "__main__":
    main()