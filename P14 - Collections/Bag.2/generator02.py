# List iterator merupakan sebuah obejct yang dapat kita gunakan untuk meng-iterasi
# elemen pada sebuah list atau tuple 1 per 1
# dapat kita perlakukan seperti generator juga

# def main():
    # data = ["Paula", "Valerya", "Dorothy", "Moses", "Marzuki", "Samosir"]

    # myGenerator = iter(data)
    # print(next(myGenerator))
    # print(next(myGenerator))
    # next(myGenerator)
    # print(next(myGenerator))
    # print(next(myGenerator))

    # print()
    # # contoh yang tuple
    # dataTuple = ("Juan", "Sterling", "Jesslyn", "Natalia")

    # myGenerator2= iter(dataTuple)
    # print(next(myGenerator2))
    # print(next(myGenerator2))
    # print(next(myGenerator2))
    # print(next(myGenerator2))
    
# Memodifikasi menjadi ke lebih pendek
def list_iterator(data):
    for item in data:
        yield item

def main():
    data_list = ["Paula", "Valerya", "Dorothy", "Moses", "Marzuki", "Samosir"]
    data_tuple = ("Juan", "Sterling", "Jesslyn", "Natalia")

    print("List Iterator:")
    for element in list_iterator(data_list):
        print(element)

    print("\nTuple Iterator:")
    for element in list_iterator(data_tuple):
        print(element)

if __name__ == "__main__":
    main() 