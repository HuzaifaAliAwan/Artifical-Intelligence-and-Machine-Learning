# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  10. Find the remainder when a number is divided by 5.

def remainder(num):
    return num%5

def main():
    try:
        num = int(input('Enter number : '))
        print(f'Remainder when divided by 5 => {remainder(num)}')
    except:
        print('Invalid entry of number, Try again ... !')
if __name__ == '__main__':
    main()