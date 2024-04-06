# List comprehension

def main():
    # List pangkat dua
    # cara biasa
    squares1 = []
    for x in range(10):
        squares1.append(x**2)
    print("squares1: ", squares1)

    squares2 = list(map(lambda x: x**2, range(10)))
    print("squares2: ", squares2)

    # list comprehension
    squares3 = [x**2 for x in range(10)]
    print("squares3: ", squares3)

    # cara biasa
    xy_berbeda1 = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                xy_berbeda1.append((x, y))
    print("xy_berbeda1:", xy_berbeda1)

    # list comprehension 
    xy_berbeda2 = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
    print("xy_berbeda2:", xy_berbeda2)

    single = [-2, -1, 0, 1, 2, 3, 4]
    triple = [x*3 for x in single]
    print("single: ", single)
    print("triple: ", triple)

    positive = [x for x in single if x >= 0]
    print("positive: ", positive)

    absolut = [abs(x) for x in single]
    print("absolut: ", absolut)

    bit_length = [bil.bit_length() for bil in single]
    print("bit_length: ", bit_length)

    pangkat2 = [(x, x**2) for x in single]
    print("pangkat2: ", pangkat2)

    from math import pi
    phi = [round(pi, c) for c in range(1, 9)]
    print("phi: ", phi)

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    flat = [bil for titik in matrix for bil in titik]
    print("titik_3d: ", matrix)
    print("flar: ", flat)

    # transpose
    transpose1 = []
    for c in range (4):
        transpose1.append([row[c] for row in matrix])
    print("transpose1: ", transpose1)

    transpose2 = [[row[c] for row in matrix] for c in range(4)]
    print("transpose2: ", transpose2)

    transpose3 = list(zip(*matrix))
    print("transpose3: ", transpose3)

if __name__ == "__main__":
    main()

