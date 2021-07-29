#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    funcs = {"triangle": triangle, "rectangle": rectangle, "circle": circle}

    while True:
        shape = input(f'Choose a shape (triangle, rectangle, circle): ')
        if shape == '':
            break
        try:
            funcs[shape]()
        except:
            print('Unknown shape!')
        
def triangle():
    a = float(input('Give base of the triangle: '))
    b = float(input('Give height of the triangle: '))
    t = a*b/2
    print(f'The area is {t:.6f}')

def rectangle():
    a = float(input('Give width of the rectangle: '))
    b = float(input('Give height of the rectangle: '))
    t = a*b
    print(f'The area is {t:.6f}')

def circle():
    r = float(input('Give the radius of the circle: '))
    t = math.pi * r**2
    print(f'The area is {t:.6f}')

if __name__ == "__main__":
    main()
