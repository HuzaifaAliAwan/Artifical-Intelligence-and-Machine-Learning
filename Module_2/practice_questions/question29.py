# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 29. Find minimum value in each column of a 3x3 matrix.

import numpy as np

def main():
    try:
        arr = np.random.randint(-100,100,(3,3))

        print(f'Original Array : \n{arr}')

        print(f'Min Number in Each col of Array : \n{np.min(arr, axis=0)}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()