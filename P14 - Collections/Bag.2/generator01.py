# Yield adalah sebuah kata kunci yang dapat dipakai untuk membuat sebuah generator
# generator pada pyhton terlihat mirip seperti sebuah function

def myGenerator():
    # dalam sebuah generator, boleh ada lebih dari 1 yield.
    # yield akan dijalankan 1 per 1 tiap iterasi berdasarkan urutan yield
    yield "Paula"
    yield "Valerya"
    yield "Dorothy"

def myOtherGenerator():
    yield "Moses"
    yield "Marzuki"
    yield "Samosir"
    
def starWarsCharacters():
    characters = ["Luke Skywalker", "Leia Organa", "Han Solo", "Chewbacca", "Darth Vader"]
    for character in characters:
        yield character

def starWarsPlanets():
    planets = ["Tatooine", "Alderaan", "Yavin IV", "Hoth", "Dagobah"]
    for planet in planets:
        yield planet

def main():
    for name in myGenerator():
        print(name)

    print()

    for name in myOtherGenerator():
        print(name)

    # generator sendiri sebenarnya merupakan sebuah object
    print()
    print(myGenerator())

    # kita juga bisa menggunakan fungsi next() untuk mengambil value pertama dari generator
    print()
    print(next(myGenerator()))
    print(next(myOtherGenerator()))

    # atau jika kita ingin meng-iterasi secara manual
    print()
    genLola = myGenerator() # masukkan obejct myGenerator ke variabel
    print(next(genLola))
    print(next(genLola))
    print(next(genLola))
    
    # nyoba 
    print()
    print(starWarsCharacters())
    print("Characters:")
    for character in starWarsCharacters():
        print(character)
    
    print()
    print(starWarsPlanets())
    print("\nPlanets:")
    for planet in starWarsPlanets():
        print(planet)

    print("\nFirst Character:")
    characters = starWarsCharacters()
    print(next(characters))

    print("\nFirst Planet:")
    planets = starWarsPlanets()
    print(next(planets))
    
    

if __name__ == "__main__":
    main()
    
    
