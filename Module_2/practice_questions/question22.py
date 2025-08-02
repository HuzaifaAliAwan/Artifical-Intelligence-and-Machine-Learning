# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 22. Find index of maximum value in a 1D array.

import numpy as np

def main():
    try:
        arr = np.random.choice(np.arange(1, 101, 5), size=(10,))
        
        print('Array :\n', arr)
        print('Index of max value :', np.argmax(arr))

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()