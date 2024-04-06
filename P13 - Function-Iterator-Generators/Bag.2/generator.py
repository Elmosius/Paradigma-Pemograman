# buat source nama
human_name_generator = ('celine', 'velkday', 'papi', 'indara', 'wijaya')

# buat source umur
human_age_generator = (age for age in range(18, 40))

# Higher-order function dengan generator expression
def generate_human_data(name_generator, age_generator, n):
    names = name_generator
    ages = age_generator
    return[{"Name": name, "Age": age} for name, age in zip(names, ages)]

def main():
    human_data = generate_human_data(human_name_generator, human_age_generator, 5)

    # Print generated human data
    for human in human_data:
        print(f"Name: {human['Name']}, Age: {human['Age']}")

if __name__ == '__main__':
    main()