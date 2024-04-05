# Intterface = Abstract class di Python
import abc      # Harus Import abc untuk abstract class / interface
class Printable(abc.ABC):
    @property
    @abc.abstractmethod
    
    def to_print(self):
        pass
    
    # Tidak ada main() karena tidak bisa
    # Membuat objek dari abstract class
    