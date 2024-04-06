# Modul lebih high level pathlib

from pathlib import Path

def main():
    # Windows
    path = Path("users") / "maranatha" / "fit" / "teknik_informatika" / "file.ext"
    print(path)
    
    print("Home path:", Path().home())
    print("Path lengkap saat ini:", Path().absolute())
    print("Parent path:", Path().absolute().parent)
    print("Apakah directory:", Path().absolute().is_dir())
    print("Apakah file:", Path().absolute().is_file())
    print("File program ini:", Path("FilePath02.py").absolute())
    print("Apakah file FilePath02.py ada:", Path("FilePath02.py").exists())
    print("Apakah FilePath02.py directory:", Path("FilePath02.py").is_dir())
    print("Apakah FilePath02.py file:", Path("FilePath02.py").is_file())
    print("File FilePath02.py owner:", Path("FilePath02.py").owner())
    print("File FilePath02.py statistics:", Path("FilePath02.py").stat())
    
if __name__ == "__main__":
    main()
