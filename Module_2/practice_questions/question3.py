# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 3. Generate a 4x4 random integer matrix (1-10).

import numpy as np

def main():
    try:
        print(np.random.randint(1,10,(4,4)))
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()