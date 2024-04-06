# Tuple & NamedTuple akses secara fungsional

from typing import Tuple, Callable, NamedTuple
from collections import namedtuple

class Color4(NamedTuple):
    'Sebuah RGB color'
    red4: int
    green4: int
    blue4: int
    name4: str

def change_color(color, new_color):
    return color._replace(red4=new_color[0], 
        green4=new_color[1], blue4=new_color[2])

def main():
    warna = (64, 128, 192)
    red = lambda color: color[0]
    green = lambda color: color[1]
    blue = lambda color: color[2]
    print("warna[0]:", warna[0])
    print("red(warna):", red(warna))
    print("green(warna):", green(warna))
    print("blue(warna):", blue(warna))

    RGB = Tuple[int, int, int]
    warna2: RGB = (128, 64, 32)
    red2: Callable[[RGB], int] = lambda color: color[0]
    green2: Callable[[RGB], int]  = lambda color: color[1]
    blue2: Callable[[RGB], int]  = lambda color: color[2]
    print("red2(warna2):", red2(warna2))
    print("green2(warna2):", green2(warna2))
    print("blue2(warna2):", blue2(warna2))

    Color = namedtuple("Color", ("red3", "green3", "blue3", "name"))
    warna3 = Color(100, 200, 255, "biru muda")
    print("warna3.red3:", warna3.red3)
    print("warna3.green3:", warna3.green3)
    print("warna3.blue3:", warna3.blue3)
    print("warna3.name:", warna3.name)

    warna4 = Color4(50, 100, 150, "biru tua")
    print("warna4.red4:", warna4.red4)
    print("warna4.green4:", warna4.green4)
    print("warna4.blue4:", warna4.blue4)
    print("warna4.name:", warna4.name4)

    new_color = (60, 70, 80)
    warna4 = change_color(warna4, new_color)
    print("warna4.red4 after color change:", warna4.red4)
    print("warna4.green4 after color change:", warna4.green4)
    print("warna4.blue4 after color change:", warna4.blue4)

if __name__ == '__main__':
    main()
