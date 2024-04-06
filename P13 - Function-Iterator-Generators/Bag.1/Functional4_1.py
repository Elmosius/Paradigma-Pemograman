# Fungsi sebagai first class objek
from typing import Callable

class Mersenne:
    'Bilangan prima Mersenne'
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm

    def __call__(self, arg: int) -> int:
        return self.pow2(arg)-1

    def set_algorithm(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm
    
# Strategi yang dapat dipakai
def shifty(b: int) -> int:
    'Ini fungsi shifty'
    return 1 << b

def multy(b: int) -> int:
    'Ini fungsi multy'
    if b == 0: return 1
    return 2*multy(b-1)

def faster(b: int) -> int:
    'Ini fungsi faster'
    if b == 0: return 1
    if b%2 == 1: return 2*faster(b-1)
    t = faster(b//2)
    return t*t

def double(b: int) -> int:
    'Ini fungsi double'
    return 2 * b

def main():
    c_s = Mersenne(shifty)
    c_m = Mersenne(multy)
    c_f = Mersenne(faster)
    c_d = Mersenne(double)  # instance baru dengan fungsi double
    print("c_s.__call__(3):", c_s.__call__(3))
    print("c_m.__call__(3):", c_m.__call__(3))
    print("c_f.__call__(3):", c_f.__call__(3))
    print("c_d.__call__(3):", c_d.__call__(3))  # panggil fungsi double

    c_all = Mersenne(shifty)
    print("c_all.__call__(3):", c_all.__call__(3))
    print("c_all.pow2.__name__:", c_all.pow2.__name__)
    c_all.set_algorithm(multy)
    print("c_all.__call__(3):", c_all.__call__(3))
    print("c_all.pow2.__name__:", c_all.pow2.__name__)
    c_all.set_algorithm(faster)
    print("c_all.__call__(3):", c_all.__call__(3))
    print("c_all.pow2.__name__:", c_all.pow2.__name__)
    c_all.set_algorithm(double)  # set fungsi double ke c_all
    print("c_all.__call__(3):", c_all.__call__(3))  # panggil fungsi double
    print("c_all.pow2.__name__:", c_all.pow2.__name__)

    print()
    print("c_s.pow2.__doc__ :", c_s.pow2.__doc__)
    print("c_s.pow2.__name__:", c_s.pow2.__name__)
    print("c_s.pow2.__code__:", c_s.pow2.__code__)
    print()
    print("c_m.pow2.__doc__ :", c_m.pow2.__doc__)
    print("c_m.pow2.__name__:", c_m.pow2.__name__)
    print("c_m.pow2.__code__:", c_m.pow2.__code__)
    print()
    print("c_f.pow2.__doc__ :", c_f.pow2.__doc__)
    print("c_f.pow2.__name__:", c_f.pow2.__name__)
    print("c_d.pow2.__doc__ :", c_d.pow2.__doc__)  # print docstring fungsi double
    print("c_d.pow2.__name__:", c_d.pow2.__name__)  # print nama fungsi double


if __name__ == '__main__':
    main()