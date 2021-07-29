#!/usr/bin/env python3
def triple(i):
    return 3*i

def square(i):
    return i**2



def main():
    for i in range(1,11):
        sq, tr = square(i), triple(i)
        if sq <= tr:
            print(f'triple({i})=={tr} square({i})=={sq}')
        else:
            break
        
if __name__ == "__main__":
    main()