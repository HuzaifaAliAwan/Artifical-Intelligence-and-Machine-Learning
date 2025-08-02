# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  30. Perform element-wise division of two arrays.

import numpy as np

def main():
    try:
        arr1 = np.random.randint(-100,100,(3,3))
        arr2 = np.random.randint(-100,100,(3,3))

        print(f'Original Array 1 : {arr1}')
        print(f'Original Array 2 : {arr2}')

        final_arr = arr1/arr2

        print(f'Final array : \n{final_arr}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()