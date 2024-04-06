# Dictionary01
def main():
    d1 = dict(red=128, green=128, blue=128)
    d2= {'red':128, 'green':128, 'blue':128}
    print("d1: ", d1)
    print("d2: ", d2)
    print("d1.red:", d1["red"], ", d1.green:", d1["green"], "d1.blue:", d1["blue"])
    d2['green'] = 255
    print("d2: ", d2)
    
    # Cek kesamaan
    if (d1 == d2):
        print("d1 == d2")
        
    else:
        print("d1 != d2")
        
    # Dictionary dengan value berupa tuple
    warna = {
        "Merah": (255,0,0),
        "Hijau": (0,255,0),
        "Biru" : (0,0,255)
    }
    
    print("warna:" , warna)
    print("warna['Biru']: ", warna['Biru'])
    warna["Merah"] = (200,0,0)
    print("warna: ", warna)
    
if __name__ == "__main__":
    main()