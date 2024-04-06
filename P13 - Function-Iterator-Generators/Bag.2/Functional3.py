# Dalam Python, string merupakan object yang immutable, sehingga cocok digunakan untuk functional programming
# Namun sintaks-sintaks method pada object string tidak sesuai dengan sintaks functional.
# Sehingga dapat menyebabkan kebingungan ketika 2 cara penulisan program digunakan secara bersama
# Maka dari itu, kita dapat membungkus method-method dari object string ke dalam function terpisah

def replace(string: str, old: str, new: str)-> str:
    return string.replace(old,new)

def main():
    lola = "Paula Valerya Dorothy"
    
    # Contoh replace string menggunakan OOP
    lola2 = lola.replace("Valerya", "Vanya")
    print(lola2)
    
    # Contoh replace string menggunakan sintaks functional
    lola3 = replace(lola, "Valerya", "Vanya")
    print(lola3)

if __name__ == "__main__":
    main()