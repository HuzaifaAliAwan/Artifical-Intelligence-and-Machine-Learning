# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 20. Sum diagonal elements of a matrix.

import numpy as np

def main():
    try:
        arr = np.random.randint(10,100,(10,10))
        
        print(f'Original Array : \n{arr}')

        # Method 1: sum of diagonal
        diagonal_sum_1 = np.diag(arr).sum()

        # Method 2: using trace
        diagonal_sum_2 = np.trace(arr)

        print(f'Diagonal Sum manual : \n{diagonal_sum_1}')
        print(f'Diagonal Sum using trace: \n{diagonal_sum_2}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()