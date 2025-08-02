# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  28. Sort a 1D array in ascending order.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,20, 20)
        arr = np.sort(arr)

        print(f'Sorted array : \n{arr}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()