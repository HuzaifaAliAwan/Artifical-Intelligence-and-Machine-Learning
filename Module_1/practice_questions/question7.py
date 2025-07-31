# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 7. Convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 1.8) + 32

def main():
    try:
        print(f'Temperature is Fahrenheit : {round(celsius_to_fahrenheit(float(input('Enter temperature in Celsius (C) : '))),1)} F')
    except:
        print('Invalid entry of temperature, Try Again....!')

if __name__ == '__main__':
    main()