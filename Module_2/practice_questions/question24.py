# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 24. Compute mean of each row in a 3x3 matrix.

import numpy as np

def main():
    try:
        arr = np.random.choice(np.arange(1, 101, 5), size=(3,3))
        
        print('Array :\n', arr)

        print('Mean of each row :', np.mean(arr, axis=1))

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()