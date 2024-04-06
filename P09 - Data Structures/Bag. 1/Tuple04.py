# Belajar Tuples

from collections import namedtuple
from dataclasses import dataclass
from typing import List


@dataclass
class PersonData:
    
    name: str
    activities: List[str]

    def add_activity(self, activity: str):
        self.activities.append(activity)

    def add_activities(self, new_activities: List[str]):
        self.activities.extend(new_activities)

    def insert_activity(self, index: int, activity: str):
        self.activities.insert(index, activity)

    def remove_activity(self, activity: str):
        if activity in self.activities:
            self.activities.remove(activity)

    def reverse_activities(self):
        self.activities.reverse()

def main():
    Person = namedtuple("Person", ["name", "activities"])
    
    # Menggunakan named tuple untuk anggota yang tidak dapat diubah
    person1 = Person("Rudy", ["membaca", "makan", "olahraga"])
    print("person1: ", person1)

    # Menggunakan dataclass untuk struktur data yang dapat dimodifikasi
    person2 = PersonData("Rudy", ["membaca", "makan", "olahraga"])
    print("person2: ", person2)

    # Modifikasi data dengan named tuple
    person1 = person1._replace(activities=person1.activities + ["jalan-jalan"])
    print("person1 (updated): ", person1)

    # Modifikasi data dengan dataclass
    person2.add_activity("jalan-jalan")
    print("person2 (updated): ", person2)

    person2.add_activities(["menyanyi", "menggambar"])
    print("person2 (updated): ", person2)

    person2.insert_activity(2, "jalan-jalan yg jauh")
    print("person2 (updated): ", person2)

    person2.remove_activity("jalan-jalan")
    print("person2 (updated): ", person2)

    person2.reverse_activities()
    print("person2 (updated): ", person2)

if __name__ == "__main__":
    main()