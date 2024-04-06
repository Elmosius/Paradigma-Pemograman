from math import sqrt

def next_(n, x):
    return (x + n/x)/2

def repeat(f,a):
    yield a
    for v in repeat(f, f(a)):
        yield v
        
def within(e, iterable):  # e = epsilon
    def head_tail(e, a, iterable):
        b = next(iterable)
        if abs(a-b) <= e:
            return b
        
        else:
            return head_tail(e, b, iterable)
    return head_tail(e, next(iterable), iterable)

def func_sqrt(a0, e, n):
    return within(e, repeat(lambda x: next_(n,x), a0))

def main():
    # cari akar pangkat 2 dari n
    a0 = 1.0
    e = 0.0001
    n = 3   # cari akar dari 3
    
    hasil = func_sqrt(a0, e,n)
    print("pendekatn akar", n, ":", hasil)
    print("fungsi akar   ", n, ":", sqrt(n))
    
if __name__ == "__main__":
    main()