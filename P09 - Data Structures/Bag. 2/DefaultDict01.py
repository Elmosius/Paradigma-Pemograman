from __future__ import annotations
from collections import defaultdict

# Tanpa defaultdict

def letter_frequency(sentence: str)-> dict[str, int]:
    frequencies: dict[str, int] = {}
    for letter in sentence:
        # Kalau sudah punya nilai ambil, kalau belum set jadi 0 & ambil
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


# Dengan defaultdic
def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    #Jika mengakses key yg blum ada, akan dibuatkan dg nilai default
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

def main():
    print("Tanpa defaultdict():")
    f1 = letter_frequency("Ini adalah kalimat")
    for key, value in f1.items():
        print("key: ", key, ", value: ", value)
        
    print("\n Dengan defaultdict():")
    f2 = letter_frequency("Ini adalah kalimat")
    for key, value in f2.items():
         print("key: ", key, ", value: ", value)
    
if __name__ == "__main__":
    main()
