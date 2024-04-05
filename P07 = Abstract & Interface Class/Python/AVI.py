from VideoFile import VideoFile
# Meskipun dalam folder yg sama, tetap harus di import
# karena dianggap berbeda modul.

class AVI(VideoFile):
    ext = '.avi'
    
    def play(self):
        print(f"Playing {self.ext} video")

    def display(self):
        print(f"Displaying {self.ext} video")