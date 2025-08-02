# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 26. Check if two arrays are equal.


import numpy as np

def main():
    try:
        arr1 = np.random.choice(np.arange(1, 101, 5), size=(3,3))
        arr2 = np.random.choice(np.arange(1, 101, 5), size=(3,3))
        
        print('Array_1:\n', arr1)
        print('Array_2:\n', arr2)

        print(f'Arrays are equal' if np.array_equal(arr1, arr2) else 'Arrays are not equal')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()