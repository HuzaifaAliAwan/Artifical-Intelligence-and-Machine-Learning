# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 18. Compute element-wise square of an array.

import numpy as np

def main():
    try:
        arr = np.random.randint(10,100,(4,4))
        
        print(f'Original Array : \n{arr}')

        # square every element
        arr = arr**2
        print(f'Squared Array : \n{arr}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()