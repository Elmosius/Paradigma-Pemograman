from abc import ABC, abstractmethod

class Bidang(ABC):
    @abstractmethod
    def hitungLuas():
        ...
        
    def getClassName():
        return "Bidang"
    
    