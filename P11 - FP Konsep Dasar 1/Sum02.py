from timeit import timeit
from math import sqrt

def next_(n, x):
    return (x + n/x)/2

def main():
    # left to right
    print("ki-ka", timeit("((([]+[1])+[2])+[3])+[4]"))
    # right to left
    print("ki-ka", timeit("[]+([1]+([2]+([3]+[4])))"))
    
    # cari akar pangkat 2 dari n
    n = 2
    f = lambda x: next_(n,x)
    a0 = 1.0
    hasil = [round(x,15) for x in (a0, f(a0), f(f(a0)),
                f(f(f(a0))), f(f(f(f(a0)))), f(f(f(f(f(a0))))))]
    print("pendekatan akar", n, " :", hasil)
    print("fungsi akar: ", n, " :", sqrt(n))
    
if __name__ == "__main__":
    main()