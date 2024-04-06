class HumanDataIterator:
    def __init__(self, names, addresses):
        self.names = names
        self.addresses = addresses
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.names):
            raise StopIteration
        else:
            name = self.names[self.current]
            address = self.addresses[self.current]
            self.current += 1
            return {"Name": name, "Address": address}

def main():
    # Sample data
    names = ["Bernadus", "Laya", "Grace", "Jessica", "Eva"]
    addresses = ["Antapani", "Pondok Labu", "Baleendah", "Buah Batu", "Cibiru"]

    human_data_iterator = HumanDataIterator(names, addresses)

    # generated human data
    for human in human_data_iterator:
        print(f"Name: {human['Name']}, Address: {human['Address']}")

if __name__ == '__main__':
    main()