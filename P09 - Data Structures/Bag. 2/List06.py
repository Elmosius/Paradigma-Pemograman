# Looping techniques

def main():
    # enumerasi dengan indexnya
    for i, v in enumerate(["tic", "tac", "toe"]):
        print(i, v)

    # loop terhadap 2 atau lebih list, digabung dengan fungsi zip()
    pertanyaan = ["NRP", "nama", "pesanan"]
    jawaban = ["2072003", "Andre", "ice cream"]
    for q, a in zip(pertanyaan, jawaban):
        print("Data {0}: {1}.".format(q, a))
    
    # loop dengan increment tertentu
    print("loop dengan increment 2")
    for c in range(1, 10, 2):
        print("c: ", c)

    # loop dengan increment tertentu & dibalik
    print("loop dengan increment 2 dan dibalik")
    for c in reversed(range(1, 10, 2)):
        print("c: ", c)
    
if __name__ == "__main__":
    main()