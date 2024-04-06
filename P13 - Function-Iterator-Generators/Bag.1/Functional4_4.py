# Cari faktor prima dari sebuah bilangan
from typing import Iterator, List
from math import sqrt

def pfactorsl(x: int) -> Iterator[int]:
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsl(x // 2)
        return
    for i in range(3, int(sqrt(x) + 0.5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from pfactorsl(x // i)
            return
    yield x

def pfactorsr(x: int) -> Iterator[int]:
    def factor_n(x: int, n: int) -> Iterator[int]:
        if n*n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n, n)
        else:
            yield from factor_n(x, n+2)
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsr(x // 2)
        return
    yield from factor_n(x, 3)

def prime_factors_to_list(n: int) -> List[int]:
    return list(pfactorsl(n))

def main():
    x1 = 10
    x2 = 13
    x3 = 100
    print("Cara loop")
    print("Prime factor dari", x1, "adalah:", end=" ")
    for a in pfactorsl(x1):
        print(a, end=" ")
    print("\nPrime factor dari", x2, "adalah:", end=" ")
    for a in pfactorsl(x2):
        print(a, end=" ")
    print("\nPrime factor dari", x3, "adalah:", end=" ")
    for a in pfactorsl(x3):
        print(a, end=" ")

    print("\n\nCara rekursif")
    print("Prime factor dari", x1, "adalah:", end=" ")
    for a in pfactorsl(x1):
        print(a, end=" ")
    print("\nPrime factor dari", x2, "adalah:", end=" ")
    for a in pfactorsl(x2):
        print(a, end=" ")
    print("\nPrime factor dari", x3, "adalah:", end=" ")
    for a in pfactorsl(x3):
        print(a, end=" ")
    print()

    print("\n\nCara list")
    print("Prime factor dari", x1, "adalah:", prime_factors_to_list(x1))
    print("Prime factor dari", x2, "adalah:", prime_factors_to_list(x2))
    print("Prime factor dari", x3, "adalah:", prime_factors_to_list(x3))

if __name__ == '__main__':
    main()
