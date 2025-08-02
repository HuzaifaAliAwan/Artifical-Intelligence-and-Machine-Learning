# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 25. Create a 5x5 matrix with ones on the border.

import numpy as np

def main():
    try:
        arr = np.zeros((5,5))
        arr[0, :], arr[-1, :], arr[:, 0], arr[:, -1] = 1, 1, 1, 1

        print(f'5x5 Matrix with ones on the border : \n{arr}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()