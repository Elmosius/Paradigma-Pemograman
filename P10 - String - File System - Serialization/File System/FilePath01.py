# Modul low level 05.path

import os.path

def main():
    path = os.path.abspath(
        os.sep.join(
            [ "", "users", "maranatha", "fit", 
             "teknik_informatika", "file.ext"]
        )
    )
    print(path)
    
    # cari path lengkap dari file program ini
    path2 = os.path.abspath("FilePath01.py")
    print(path2)
    
    path3 = os.path.abspath(os.path.curdir)
    print(path3)
    
if __name__ == "__main__":
    main()