# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 10. Slice a 4x4 matrix to get the top-left 2x2 submatrix.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10,(4,4))
        print(f'Complete Array : \n {arr}')

        print(f'Sliced Array : \n{arr[:2,:2]}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()