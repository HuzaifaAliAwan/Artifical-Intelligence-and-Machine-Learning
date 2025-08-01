# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 11. Add a scalar to all elements of an array.

import numpy as np

def main():
    try:
        arr = np.random.randint(1,10,(4,4))
        print(f'Before adding scalar : \n{arr}')

        arr +=10
        print(f'After adding scalar of 10 : \n{arr}')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()