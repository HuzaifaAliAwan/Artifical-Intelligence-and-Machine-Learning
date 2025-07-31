# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  8. Check if a year is a leap year.
# A leap year is which divisible by 4 but not 100 
# OR the one which is divisible by 400

def check_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

def main():
    try:
        year = int(input('Enter a year number: '))

        if(check_leap_year(year)):
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    except:
        print('Invalid year number, Try again...!')

if __name__ == '__main__':
    main()