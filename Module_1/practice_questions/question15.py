# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 15. Reverse a user-input number.

def reverse(data):
    return data[::-1]

def main():
    try:
        print(f'Reverse is : {reverse(input('Enter a String : '))}')
    except:
        print('Invalid Entry....! Try Again')

if __name__ == '__main__':
    main()