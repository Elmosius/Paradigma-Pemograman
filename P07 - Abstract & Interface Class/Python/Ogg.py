from MediaLoader import MediaLoader
# Meskipun dalam folder yg sama, tetap harus di import
# karena dianggap berbeda modul.

class Ogg(MediaLoader):
    ext = '.ogg'
    
    def play(self):
        pass
    
def main():
    g = Ogg()
    # Tidak error karena abstract method sudah dibuat
    
if __name__ == '__main__':
    main()