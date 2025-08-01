# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 7. Create a 5x5 identity matrix.

import numpy as np

def main():
    try:
        arr = np.eye(5)
        print(f'Array : \n{arr}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()