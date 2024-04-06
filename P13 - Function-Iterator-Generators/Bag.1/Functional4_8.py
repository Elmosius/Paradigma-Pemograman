# Coba yg malas(lazy) dan yg rajin (eager)
def main():
    # yang lazy
    print("Lazy evaluation:")
    r = range(10)  # Ini adalah objek range, belum dievaluasi
    print(r)
    print([r])  # Ini adalah list yang berisi objek range

    # yang eager
    print("\nEager evaluation:")
    l = [x for x in r]  # Ini adalah list yang dievaluasi dari objek range
    print(l)
    print(list(r))  # Fungsi list() juga melakukan eager evaluation pada objek range

    # generator (lazy)
    print("\nNew case - Generator (lazy):")
    g = (x for x in range(10))  # Ini adalah generator, contoh lain dari lazy evaluation
    print(g)

    # memaksa evaluasi pada generator (menjadi eager)
    print("\nNew case - Forcing evaluation on generator (becomes eager):")
    print(list(g))  # Mengubah generator menjadi list memaksa evaluasi eager

if __name__ == "__main__":
    main()


    