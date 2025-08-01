# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 9. Extract the first row of a 3x3 matrix.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10,(3,3))
        print(arr[0])
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()