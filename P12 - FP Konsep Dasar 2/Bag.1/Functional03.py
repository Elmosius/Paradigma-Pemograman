# Eager dan lazy evaluation

def numbers():
    for i in range(1024):
        print(f"= {i}")
        yield i

def sum_to(n: int)-> int:
    sum: int = 0
    for i in numbers():
        if i == n : break
        sum += i
    return sum

def product_to(n: int)-> int:
    product: int = 1
    for i in numbers():
        if i == n : break
        product *= i
    return product

def main():
    # lazy evalutation
    print(2==3 and "right")     # left only
    print(2==3-1 and "right")   # left & right
    print(2==3 or "right")      # left & right
    print(2==3-1 or "right")    # left only

    # eager evaluation
    print(2==3 and "right" or "wrong")     # left & right
    print(2==3-1 and "right" or "wrong")   # left & right
    print(2==3 or "right" and "wrong")     # left only
    print(2==3-1 or "right" and "wrong")   # left & right

    print(sum_to(3))
    print(product_to(3))

if __name__ == "__main__":
    main()
