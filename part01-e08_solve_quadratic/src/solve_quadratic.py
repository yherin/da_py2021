#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    i =  (math.sqrt(b**2 - (4*a*c))) 
    x1 = ((b*-1) + i) / 2*a
    x2 = ((b*-1) - i) / 2*a
    return (x1,x2)

def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    print(solve_quadratic(8.582447,8.352103,1.319727))


if __name__ == "__main__":
    main()
