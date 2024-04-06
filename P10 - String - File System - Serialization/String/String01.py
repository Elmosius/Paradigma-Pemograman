from dataclasses import dataclass
from collections import namedtuple
# Latihan String

@dataclass
class LatihanString:
    a: str
    b: str
    c: str
    d: str
    e: str

def main():
    a = "hello"
    b = 'world'
    c = '''String
    beberapa
    baris'''
    d = """Ada lagi string 
    beberapa baris"""
    e = ("ini " "beberapa " "kata " "jadi satu")

    string_obj = LatihanString(a, b, c, d, e)
    print("String a:", string_obj.a)
    print("String b:", string_obj.b)
    print("String c:", string_obj.c)
    print("String d:", string_obj.d)
    print("String e:", string_obj.e)
    print()
    
    string_tuple = (a, b, c, d, e)
    for i, value in enumerate(string_tuple, start=1):
        print(f"String {i}: {value}")
    print()

  

if __name__ == "__main__":
    main()