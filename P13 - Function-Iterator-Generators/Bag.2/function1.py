# Using tuple
# Mengimpor modul 'namedtuple' dari koleksi python untuk membuat namedtuple
from collections import namedtuple

# assign namedtuple
Operation = namedtuple('Operation', ['add', 'multiply', 'substract'])

# Membuat lambda function
add: Operation = lambda x, y: x + y

multiply: Operation = lambda x, y: x * y

substract: Operation = lambda x, y: x - y

def main():
    
    num1, num2 = 5,3

    result_add = add(num1, num2)
    result_multiply = multiply(num1, num2)
    result_substract = substract(num1, num2)

    print(f"{num1} + {num2} = {result_add}")
    print(f"{num1} * {num2} = {result_multiply}")
    print(f"{num1} - {num2} = {result_substract}")

if __name__ == '__main__':
    main()