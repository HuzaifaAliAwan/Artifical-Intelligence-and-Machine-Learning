#  4. Compute the square of a user-input number.

def main():
    try:
        print(f'Square of number : {pow(int(input('Enter number : ')),2)}')

    except:
        print('Enter a Valid number')

if __name__ == '__main__':
    main()