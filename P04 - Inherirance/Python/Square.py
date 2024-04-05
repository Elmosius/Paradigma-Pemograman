# Turunan dari abstract class Shape
from Shape import Shape
class Square(Shape):
    def __init__(self):
        self.__length: float = 0.0
        
    @property
    def length(self) -> float:
        return self.length
    
    @length.setter
    def length(self, length:float) -> None:
        self.__length = length
        
    def area(self) -> float:
        return self.__length * self.__length
    
    def __str__(self):
        return "Square, length: " + str(self.__length)
    
    
def main():
    s = Square()
    print(s)
    print(s," | Area: " + str(s.area()))
    s.length = 5.0
    print(s," | Area: " + str(s.area()))
        
if __name__ == "__main__":
    main()