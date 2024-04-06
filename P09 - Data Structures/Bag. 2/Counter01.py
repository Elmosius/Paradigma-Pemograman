from collections import Counter


def letter_frequency_3(sentence: str) -> Counter:
    return Counter(sentence)

def main():
    polling = ["caramel", "strawberry", "vanilla", "chocolate", 
               "vanilla", "vanilla", "chocolate", "vanilla"]
    
    print("Juice yg dipesan: ")
    favorites1 = Counter(polling)
    for juice, freq in favorites1.items():
        print("juice: ", juice, ", freq: ", freq)
        
    print("\n2 Juice paling favorit: ")
    favorites2 = Counter(polling).most_common(2)
    for juice, freq in favorites2:
        print("juice: ", juice, ", freq: ", freq)
    
if __name__ == "__main__":
    main()