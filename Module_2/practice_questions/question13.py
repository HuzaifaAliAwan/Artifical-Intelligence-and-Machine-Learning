# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  13. Reshape a 1D array (12 elements) into a 3x4 matrix.

import numpy as np

def main():
    try:
        arr = np.arange(12)
        reshaped_arr = arr.reshape(3,4)
        print(f'Original Array\n{arr}')
        print(f'\nReshaped Array\n{reshaped_arr}')
        
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()