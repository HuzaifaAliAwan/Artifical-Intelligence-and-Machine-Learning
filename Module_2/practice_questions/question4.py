# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 4. Sum all elements in a 2D array.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10,(2,2))
        print(f'Array : {arr}')
        print(f'Sum of array elemnets : {np.sum(arr)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()