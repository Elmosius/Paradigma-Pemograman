# Dictionary04

class KelasSaya():
    def __init__(self):
        self.data = 0

def main():
    # Dictionary dengan tipe key & value berbeda 2
    d1 = {}
    d1[7] = 14
    d1[8] = "delapan"
    d1['sembilan'] = "delapan + satu"
    d1['sepuluh'] = 10
    d1[3.14] = "PI"
    d1['PI'] = 3.1415
    d1[(0,128,128)] = "kuning"
    d1['orange'] = (128,128,0)
    d1['warna'] = ["merah", "kuning", "hijau", "di langit yg biru"]
    # List tidak bisa dipakai sebagai key
    # key harus yang punya nilai hash() tetap
    # d1[[1,2,3]] = "one, rwo, three ... go"
    print("has(str): ", hash("ini string"))
    # print("hash(list): ", hash([1,2,3]))
    
    k = KelasSaya()
    d1[k] = "value utk key objek KelasSaya"
    
    for kunci, nilai in d1.items():
        print("key: ", kunci, " , value: ", nilai)
    
    # Contoh bilangan yg berbeda engan nilai hash yg sama
    # (hash collision)
    x = 2021
    y = 2305843009213695972
    print("x: ", x)
    print("y: ", y)
    print("x == y: ", x == y)
    print("hash(x) == hash(y): ", hash(x) == hash(y))
    print("hash(x): ", hash(x))
    print("hash(y): ", hash(y))
if __name__ == "__main__":
    main()