# # Set koleksi yang elemennya unik tidak ada duplikat dan tidak terurut

def main():
    basket = {"apel", "jeruk", "pisang", "nangka", "jeruk", "apel"}
    print("basket:", basket)
    basket.add("pepaya")
    print("basket.add('pepaya'): ", basket)
    basket.add("jeruk")
    print("basket.add('jeruk'): ", basket)
    basket2 = basket.copy()
    print("basket2: ", basket2)
    basket.remove("apel")
    print("basket.remove('apel'): ", basket)
    basket.discard("pepaya")
    print("basket.discard('pepaya'): ", basket)
    
    basket3 = {"jeruk", "pepaya"}
    basket4 = {"nangka"}
    print("basket3:", basket3)
    print("basket4:", basket4)
    print("basket.difference(basket3): ", basket.difference(basket3))
    print("basket.intersection(basket3): ", basket.intersection(basket3))
    print("basket.issuperset(basket3): ", basket.issuperset(basket3))
    print("basket3.issubset(basket): ", basket3.issubset(basket))
    print("basket.isdisjoint(basket3): ", basket.isdisjoint(basket3))
    print("basket.issuperset(basket4): ", basket.issuperset(basket4))
    print("basket4.issubset(basket): ", basket4.issubset(basket))
    print("basket.isdisjoint(basket4): ", basket.isdisjoint(basket4))
    print("basket.__contains__('mangga'): ", basket.__contains__('mangga'))
    print("basket.isdisjoint({'mangga'}): ", basket.isdisjoint({'mangga'}))
    print("basket.__contains__('jeruk'): ", basket.__contains__('jeruk'))
    print("basket.isdisjoint({'jeruk'}): ", basket.isdisjoint({'jeruk'}))

if __name__ == "__main__":
    main()