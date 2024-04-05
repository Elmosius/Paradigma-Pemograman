from MediaLoader import MediaLoader 
# Meskipun dalam folder yg sama, tetap harus di import
# karena dianggap berbeda modul.

class AudioFile(MediaLoader):
    def play(self):
        print(f'Sedang menjalankan {self.ext} file')