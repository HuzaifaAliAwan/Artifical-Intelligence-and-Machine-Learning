# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 2. Create a 3x3 zero matrix.

import numpy as np

def main():
    try:
        print(np.zeros((3,3)))
        # Explanation of two paranthesis
        # The outer paranthesis are to call funtion zeros 
        # The inner paranthesis are for tuple, The tuple is being passed to the function 

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()