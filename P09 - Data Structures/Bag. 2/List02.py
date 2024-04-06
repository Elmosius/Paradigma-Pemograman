# Method-method untuk list

def main():
    buah = ["nanas", "apel", "pisang", "jeruk", "kiwi"]
    print("buah: ", buah)
    buah.append("jeruk")
    print("buah: ", buah)
    buah.extend(["mangga", "jambu"])
    print("buah: ", buah)
    buah[len(buah):] = ["nangka", "durian"]
    print("buah: ", buah)
    buah.insert(1, "lengkeng")
    print("buah: ", buah)
    print("buah.count{'jeruk'}: ", buah.count("jeruk"))
    print("buah: ", buah)
    buah.remove("jeruk")
    print("buah: ", buah)
    print("buah.pop(): ", buah.pop())
    print("buah: ", buah)
    print("buah.pop(1): ", buah.pop(1))
    print("buah: ", buah)
    print("buah.index('kiwi'): ", buah.index('kiwi'))
    print("buah: ", buah)
    buah.sort()
    print("buah: ", buah)
    buah.reverse()
    print("buah: ", buah)
    buah.append("nangka")
    print("buah: ", buah)
    print("buah.index('nangka'): ", buah.index('nangka'))
    print("buah.index('nangka', 3): ", buah.index('nangka', 3))
    print("buah.__contains__('nangka'): ", buah.__contains__('nangka'))
    buah2 = buah.copy()
    print("buah2: ", buah2)
    buah.clear()
    print("buah: ", buah)

if __name__ == "__main__":
    main()

