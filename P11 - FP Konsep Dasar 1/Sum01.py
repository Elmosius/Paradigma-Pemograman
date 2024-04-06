# recursive jml semua

def sumr(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])
    
# functional
def until(n, filter_func, v):
    if (v == n):
        return []
    if(filter_func(v) ):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n,filter_func, v+1)
    
def filter_ganjil(v: int) -> bool:
    if(v % 2 == 1):
        return True
    else:
        return False
    
def main():
    # procedural
    s = 0
    for n in range(1,10):
        if(n % 3 == 0  or n % 5 == 0):
            s +=n
    print("procedural : ", s)
    
    # object oriented
    m = list()
    for n in range(1,10):
        if(n % 3 == 0 or n % 5 == 0):
            m.append(n)
    print("oop: ", sum(m))
    
    # coba recursive jml semua
    seq = [1,2,3,4,5,6,7,8,9]
    print("recursive 1-9: ", sumr(seq))
    
    # coba functional
    list1 = until(10, lambda x: x % 3 == 0 or x % 5 == 0, 0)
    print("functional:", list1)
    print("functional:", sum(list1))
    
    list2 = until(10, lambda x: x % 2 == 0 , 0)
    print("functional:", list2)
    print("functional:", sum(list2))
    
    list3 = until(10, filter_ganjil , 0)
    print("functional:", list3)
    print("functional:", sum(list3))
    
    # hybrid
    hasil = sum(z for z in range(1,10) if z % 3 == 0 or z % 5 == 0)
    print("hybrid: ", hasil)
    # print("z: ", z) # z hanya ada di internal proses for
    

if __name__ == "__main__":
    main()