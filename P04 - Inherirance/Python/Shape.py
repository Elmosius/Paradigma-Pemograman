# Abstract Class
import abc      # Harus Import abc untuk abstract class
class Shape(abc.ABC):
    @property
    @abc.abstractmethod
    
    def area(self):
        pass
    
    # Tidak ada main() karena tidak bisa
    # Membuat objek dari abstract class
    