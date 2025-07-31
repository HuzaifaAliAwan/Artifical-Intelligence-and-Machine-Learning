# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 12. Calculate the factorial of a user-input number.

# import math

def factorial(num):
    fact = 1
    for x in range(num, 1, -1):
        fact *=x
    return fact

    # There is a build in function in maths library 
    # return math.factorial(n)

def main():
    try:
        num = int(input('Enter number : '))
        if(num<0):
            raise ValueError('Invalid Number')
        print(f'Factorial of {num} = {factorial(num)}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()