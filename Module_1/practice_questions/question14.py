# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 14. Count the digits in a number.

def no_of_digits(num):
    return len(str(num))

def main():
    try:
        num = int(input('Enter number : '))
        print(f'Digits in {num} => {no_of_digits(num)}')
    except ValueError as e:
        print('Invalid Number Entry....! Try Again.')
        # print(e)

if __name__ == '__main__':
    main()