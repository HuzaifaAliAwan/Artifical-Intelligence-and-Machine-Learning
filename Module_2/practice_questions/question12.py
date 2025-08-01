# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 12. Create an array of even numbers (2 to 20).

import numpy as np

def main():
    try:
        arr = np.random.choice(np.arange(2,20,2), size=(4,4))
        print(f'Array of Even numbers : \n{arr}')   

        # Explanation
        # np.arange(start,end,step)
        # np.random.choice(array, size)

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()