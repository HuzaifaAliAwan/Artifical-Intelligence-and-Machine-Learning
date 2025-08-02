# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 21. Create an array (1 to 100, step=5).

import numpy as np

def main():
    try:
        arr = np.random.choice(np.arange(1, 101, 5), size=(10,10))
        print(f'Array with values from 1 to 100 with step of 5 : \n{arr}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()