# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 26. Check if a string contains only digits.

def contain_only_digits(string):
    try:
        data = int(string)
        return True
    except:
        return False
def main():
    try:
        string = input('Enter String : ')
        print("String contain only Digits" if contain_only_digits(string) else 'String contain other character then digits')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()