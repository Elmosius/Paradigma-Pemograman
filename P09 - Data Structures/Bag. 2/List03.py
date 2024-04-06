# List sebagai stack, Last In First Out (LIFO)

def main():
    stack = [1, 2, 3, 4, 5, 6]
    print("stack: ", stack)
    print("stack.append(7): ", stack.append(7))
    print("stack: ", stack)
    print("stack.append(8): ", stack.append(8))
    print("stack: ", stack)
    print("stack.pop(): ", stack.pop())
    print("stack: ", stack)
    print("stack.pop(5): ", stack.pop(5)) # pop indeks 5
    print("stack: ", stack)
    print("stack.pop(): ", stack.pop())
    print("stack: ", stack)

if __name__ == "__main__":
    main()

