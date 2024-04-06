# Serialize beberapa objek

import pickle
from random import Random

class Student:
    def __init__(self, name, ipk):
        self.name = name
        self.ipk = ipk
        
    def __str__(self):
        return self.name + " " + str(f"{self.ipk:.2f}")
def main():
    fname = 'student.dat'
    print("Data Students di memory:")
    students = []
    for c in range(5):
        students.append(Student("Mahasiswa" + str(c+1), Random().random()*4.0))
        print(students[c])
        
    print("Menulis data Students ke student.dat")
    try:
        with open(fname, 'wb') as fo:
            for student in students:
                pickle.dump(student, fo, pickle.HIGHEST_PROTOCOL)
    except FileNotFoundError as fnfe:
        print("Gagal membuat file...mungkin HD anda penuh!")
        
    print("Membaca data Students dari studen.dat")
    students_read= []
    try:
        with open(fname, 'rb') as fi:
            while True:
                try:
                    student = pickle.load(fi)
                except(EOFError, pickle.UnpicklingError):
                    break
                students_read.append(student)
    except FileNotFoundError as fnfe:
        print("File tidak ketemu...mungkin sedang ngumpet...")
    for student in students_read:
        print(student)
       
if __name__ == "__main__":
    main()