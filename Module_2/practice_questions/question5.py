# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 5. Compute mean of a 1D array of 10 random numbers.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10, 10)
        print(f'Array : {arr}')
        print(f'Mean : {np.mean(arr)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()