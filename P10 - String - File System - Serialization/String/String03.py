# Fungsi2 string

def main():
    # bantuan dari dokumentasi
    help(str.endswith)
    print(dir(str.lower))
    
    print('"inistring".isalpha() :', "inistring".isalpha())
    print('"ini string".isalpha() :', "ini string".isalpha())
    print('"inistring3".isalpha() :', "inistring3" .isalpha())
    print('"inistring?" .isalpha() :', "inistring?".isalpha())
    print()
    
    print('"HURUFBESAR".isupper() :', "HURUFBESAR".isupper())
    print('"HURUF BESAR".isupper() :', "HURUF BESAR".isupper())
    print('"HURUFBesar".isupper() :', "HURUFBesar".isupper())
    print('"HURUFBESAR?".isupper() :', "HURUFBESAR?".isupper())
    print('"HURUFBESAR7".isupper() :', "HURUFBESAR7".isupper())
    print()
    
    print('"hurufkecil".islower() :', "hurufkecil".islower())
    print('"huruf kecil".islower() :', "huruf kecil".islower())
    print('"hurufkecil?".islower() :', "hurufkecil?".islower())
    print('"hurufkecil5".islower() :', "hurufkecil5".islower())
    print('"Hurufkecil".islower() :', "Hurufkecil".islower())
    print()
    
    print('"Maranatha".endswith("natha") :', "Maranatha".endswith("natha"))
    print('"Maranatha".endswith("natha ") :', "Maranatha".endswith("natha "))
    print('"Maranatha".endswith("natha",3) :', "Maranatha".endswith("natha",3))
    print('"Maranatha".endswith("natha",5) :', "Maranatha".endswith("natha",5))
    print('"Maranatha".endswith("natha",4,9) :', "Maranatha".endswith("natha",4,9))    
    print()
    
    print('"  ".isspace() :', "  ".isspace())
    print('"    ".isspace() :', "    ".isspace())
    print('"\t".isspace() :', "\t".isspace())
    print('"\n".isspace() :', "\n".isspace())
    print('"kutip 3".isspace():',"""
          
    """.isspace())
    print('" a ".isspace():'," a ".isspace())
    print()
    
    print('"Ini Judul".istitle():', "Ini Judul".istitle())
    print('"Ini judul".istitle():', "Ini judul".istitle())
    print('"Ini JuDul".istitle():', "Ini JuDul".istitle())
    print('"Ini dan Judul".istitle():', "Ini dan Judul".istitle())



if __name__ == "__main__":
    main()
