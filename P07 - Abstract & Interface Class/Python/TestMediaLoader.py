from Ogg2 import Ogg2
from Wav2 import Wav2
from MP3 import MP3
from FLAC import FLAC
from MP4 import MP4
from AVI import AVI


def main():
    g = Ogg2()
    g.play()

    w = Wav2()
    w.play()

    m = MP3()
    m.play()

    f = FLAC()
    f.play()

    mp = MP4()
    mp.play()
    mp.display()

    avi = AVI()
    avi.play()
    avi.display()
    
    
if __name__ == '__main__':
    main()