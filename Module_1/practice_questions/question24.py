# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 24. Convert a decimal number to binary.

def convert_to_binary(decimal_num):
    binary_val = ''
    while decimal_num>0:
        binary_val = str(decimal_num%2) + binary_val
        decimal_num = decimal_num//2
    return binary_val or '0'

def main():
    try:
        num = int(input('Enter number : '))
        print(f'Binary of {num} = {convert_to_binary(num)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()