# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 8. Multiply two 2x2 matrices.

import numpy as np

def main():
    try:
        arr1 = np.random.randint(1,10,(2,2))
        arr2 = np.random.randint(1,10,(2,2))

        print(f'Array 1 : \n{arr1}')
        print(f'Array 2 : \n{arr2}')

        # Method 1
        print(f'Simple Product : \n{arr1 @ arr2}')
        
        # Method 2
        print(f'Mat multiplication : \n{np.matmul(arr1, arr2)}')
        
        # Method 3
        print(f'Dot Product : \n{np.dot(arr1, arr2)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()