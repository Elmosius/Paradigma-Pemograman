# Generator setelah dipakai 1x kemudian kosong kembali
import itertools
from typing import Iterable, Any

def limits(iterable: Iterable[Any])-> Any:
    max_tee, min_tee = itertools.tee(iterable,2)
    # print(max(max_tee))   //kalau sudah dipakai di sini
    # print(min(min_tee))   //maka max_tee & min_tee kosong
    # for c in max_tee:
    #     print(c, end=" ")
    # print()
    mylist = []
    for c in max_tee:
        mylist.append(c)
    for c in mylist:
        print(c, end=" ")
    print()
    return max(mylist), min(min_tee)

def main():
    data = [3,7,2,9,6,1,8,5,7,2]
    max, min = limits(data)
    print(max)
    print(min)

if __name__ == "__main__":
    main()

    