# First class function
def example(a, b):
    return a * b

def fungsi_pangkat(x):
    return 2**x - 1

def apply_func(func, x, y):
    return func(x, y)

def main():
    # bukti fungsi adalah objek
    print("Type of example function:", type(example))
    print("example function arguments:", example.__code__.co_varnames)
    print("example function argument count:", example.__code__.co_argcount)

    # assign fungsi lambda ke variabel
    pangkat = lambda x: 2**x - 1
    print("lambda pangkat:", pangkat(3))
    print("fungsi pangkat:", fungsi_pangkat(3))

    # Menerapkan apply_func untuk memakai fungsi lainnya
    result = apply_func(example, 2, 3)
    print("Result of apply_func with example function:", result)

    # Memakai high order function
    def create_multiplier(factor):
        return lambda x: x * factor

    multiply_by_5 = create_multiplier(5)
    print("Multiply by 5:", multiply_by_5(3))

if __name__ == "__main__":
    main()
