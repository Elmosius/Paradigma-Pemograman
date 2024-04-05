from Bidang2 import Bidang2
from Movement import Movement
from Segi4b import Segi4b

def main():
    b = Bidang2()
    m = Movement()
    s = Segi4b()
    
    print("Luas ", s.getClassName(), ":", s.hitungLuas())
    print("x = ", s.x)
    s.moveLeft()
    print("x = " , s.x)
    
    
if __name__ == '__main__':
    main()