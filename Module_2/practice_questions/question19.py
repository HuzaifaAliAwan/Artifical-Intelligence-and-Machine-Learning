# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 19. Transpose a 3x3 matrix.

import numpy as np

def main():
    try:
        arr = np.random.randint(10,100,(3,3))
        
        print(f'Original Array : \n{arr}')

        # square every element
        arr = np.transpose(arr)
        print(f'Transposed Array : \n{arr}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()