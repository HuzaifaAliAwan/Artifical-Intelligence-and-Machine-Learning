# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  15. Find the maximum value in a 2D array.

import numpy as np

def main():
    try:
        arr = np.random.randint(-100,100,(4,4))
        
        print(f'Original Array : \n{arr}')

        print(f'Max Number in Array : {np.max(arr)}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()