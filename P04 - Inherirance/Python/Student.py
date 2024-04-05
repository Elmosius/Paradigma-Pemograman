# Inherirance: child class
from Person import Person # dari Person.py import kelas Person

class Student(Person):
    def __init__(self):
        super().__init__() # panggil __init__() dari kelas induk
        self.__semester: int = 1
        
    @property
    def semester(self) -> int:
        return self.__semester
    
    @semester.setter
    def semester(self, semester:int) -> None:
        self.__semester = max(1,min(8, semester))
        
    def __str__(self) ->str:
        # return "NIK: " + self.nik + " | Nama: " + self.name + " | Semester: " + str(self.__semester)
        # Menggunkaan super() jadi lebih pendek kodenya
        
        return super().__str__() + " | Semester: " + str(self.__semester)
        
def main():
    s = Student()
    print(s)
    s.nik = "12345"
    s.name = "Person"
    print(s)
        
if __name__ == "__main__":
    main()