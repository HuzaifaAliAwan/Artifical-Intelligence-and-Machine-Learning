# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 1. Create a 1D array with numbers 1 to 10.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10,10)
        print(arr)
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()