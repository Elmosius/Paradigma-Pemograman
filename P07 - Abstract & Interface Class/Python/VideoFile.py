from abc import ABC, abstractmethod
from MediaLoader import MediaLoader
# Meskipun dalam folder yg sama, tetap harus di import
# karena dianggap berbeda modul.

class VideoFile(MediaLoader):
    @abstractmethod
    def display(self) -> None:
        pass
    
    
