# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 19. Check if a string is a palindrome.

def is_palendrome(data):
    return data == data[::-1]

def main():
    try:
        if(is_palendrome(input('Enter String : '))):
            print('Palendrome')
        else:
            print('Not Palendrome')
    except ValueError as e:
        print('Invalid Entry..... !, Try Again')
if __name__ == '__main__':
    main()