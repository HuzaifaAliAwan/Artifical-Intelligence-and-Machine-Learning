# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 21. Find the GCD of two numbers.

# import math

def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b, a%b)

def main():
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print(f'GCD of {a} and {b} = {GCD(a,b)}')

        # method from math library
        # print(f'GCD of {a} and {b} = {math.gcd(a,b)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()