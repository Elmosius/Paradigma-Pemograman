from abc import ABC, abstractmethod

class MediaLoader(ABC):
    # Python menyediakan modul abc dan kelas ABC
    # untuk membentuk kelas abstrak
    # ABC = Abstract Base Class
    # Pada awal program harus melakukan: from abc import .....
    
    # Method play() & ext() bersifat abstrak
    # Method abstrak tidak memiliki body, jadi hanya diisi '...'
    @abstractmethod
    def play(self) -> None:
        ...
        
    @property
    @abstractmethod
    def ext(self) -> str:
        ...
        
    # Turunan dari kelas abstrak harus membuat implementasi
    # dari method2 abstraknya.
    