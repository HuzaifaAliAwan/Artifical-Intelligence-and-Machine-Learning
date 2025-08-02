# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 23. Concatenate two 1D arrays.

import numpy as np

def main():
    try:
        arr1 = np.random.choice(np.arange(1, 101, 5), size=(10,))
        arr2 = np.random.choice(np.arange(1, 101, 5), size=(10,))
        
        print('Array 1 :\n', arr1)
        print('Array 2 :\n', arr2)
        
        contact_array = np.concatenate((arr1, arr2))
        print('Concatenated Array :\n', contact_array)

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()