# Contoh menggunakan fungsi zip
# Fungsi zip akan membuat tuple yang berisikan data dari kedua list per elementnya

def main():
    
    a = ["Moses", "Juan", "Phin"]       # contoh list a
    b = ["Paula", "Eugenia", "Linzy"]    # contoh list b
    data = zip(a,b)                     # fungsi zip dipanggil dan diberikan a dan b
    # for x in data:
    #     print(x)                        # print hasil zip
    
    # Mencetak hasil zip dalam format yang lebih mudah dibaca
    for x, y in data:
        print(f"{x} dan {y} adalah pasangan yang baik.")         

    # Mencoba 
    # a = input("Masukkan nama-nama guru, dipisahkan oleh koma: ").split(',')
    # b = input("Masukkan mata pelajaran yang diajarkan oleh guru tersebut, dipisahkan oleh koma: ").split(',')

    # if (len(a) != len(b)):
    #     print("Jumlah guru dan mata pelajaran harus sama.")
    #     return

    # data = zip(a, b)  
    # for x, y in data:
    #     print(f"{x.strip()} mengajar {y.strip()}.")

if __name__ == '__main__':
    main()