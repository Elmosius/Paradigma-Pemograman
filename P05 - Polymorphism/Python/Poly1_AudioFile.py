from pathlib import Path

class AudioFile:
    ext:str
    
    def __init__(self, filepath: Path)-> None:
        # Polymorphism: method __init()__ dari parent
        # dapat mengakses ext dari subclass-nya
        print("Isi ext: " + self.ext)
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath
        
class MP3File(AudioFile):
    ext = ".mp3"
    
    #  Polymorphism: semua turunan AudioFile memiliki
    # implementasi method play()-nya sendiri2
    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")
        
        
class WavFile(AudioFile):
    ext = ".wav"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as wav")
        
class OggFile(AudioFile):
    ext = ".ogg"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")
        
# Kelas FlacFile bukan turunan dari kelas AudioFIle
# tetapi tetap jalan karena duck typing di Python
# mengijinkan penggunaan sembarang objek selama menyediakan
# method yg sesuai

class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath
        
        
    def play(self) -> None:
        print(f"playing {self.filepath} as flac")
        
def main():
    p_1 = MP3File(Path("How great Thou art.mp3"))
    p_1.play()     
    p_2 = WavFile(Path("My heart will go on.wav"))
    p_2.play()
    p_3 = OggFile(Path("The Prayer.ogg"))
    p_3.play()
    
    # Silahkan dicoba yang ini hasilnya akan error
    # p_4 = MP3File(Path("Breakfast at Tiffanys.mov"))
    # p_4.play()
    
    # FlacFile bukan turunan dari AudioFile
    p_5 = FlacFile(Path("Alison Krauss.flac"))
    p_5.play
    
    
if __name__ == "__main__":
    main()
