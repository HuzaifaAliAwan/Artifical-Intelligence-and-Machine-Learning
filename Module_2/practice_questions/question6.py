# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 6. Calculate standard deviation of an array.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10, 10)
        print(f'Array : {arr}')
        print(f'Standard Deviation : {round(np.std(arr),2)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()