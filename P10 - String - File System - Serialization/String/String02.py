# Coba iterate, index, slice, concatenate

def main():
    s = "Saya adalah sebuah string"

    # Iterate
    print("Iterate:")
    for c in s:
        print(c, end=" ")
    print()

    # Index
    print("\nIndex:")
    for i, c in enumerate(s):
        print(f"Index {i}: {c}")

    # Slicing
    print("\nSlicing:")
    print("5 Karakter pertama:", s[:5])
    print("Karater dari 0 - 10:", s[:11])
    print("Karakter dari 12 smpai slesai:", s[12:])
    print("Karakter dari 5 - 10:", s[5:11])
    print("Full string:", s[:])

    # Concatenate
    print("\nConcatenate:")
    s2 = "ini " + "string"
    print(s2)
    s3 = "saya " + "string " + "juga"
    print(s3)

if __name__ == "__main__":
    main()
