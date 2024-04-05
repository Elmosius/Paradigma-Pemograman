from MediaLoader import MediaLoader
# Meskipun dalam folder yg sama, tetap harus di import
# karena dianggap berbeda modul.

class Wav(MediaLoader):
    # pass
    
    ext = '.wav'
    
    # def play(self):
    #   pass
    # Simulasi kondisi tidak implementasi method play()
    
def main():
    print("test...")
    # w = Wav()
    # Coba dibuka comment baris di atas
    # TypeError : Can't instantiate abstract class
    # Wav with abstract methods play
    
if __name__ == '__main__':
    main()