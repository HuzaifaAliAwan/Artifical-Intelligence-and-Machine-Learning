# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  27. Compute inverse of a 2x2 matrix.

import numpy as np

def main():
    try:
        arr = np.random.choice(np.arange(1, 101, 5), size=(2,2))
        
        print('Array:\n', arr)

        print(f'Inverse of array : \n{np.linalg.inv(arr)}')
    
        # Explanation 
        # linalg is a Linear Algebra Module in Numpy library, it contain many functions 
        # | Function            | Purpose                         |
        # | ------------------- | ------------------------------- |
        # | `np.linalg.inv()`   | Inverse of a matrix             |
        # | `np.linalg.det()`   | Determinant                     |
        # | `np.linalg.solve()` | Solve linear equations $Ax = b$ |
        # | `np.linalg.eig()`   | Eigenvalues and eigenvectors    |
        # | `np.linalg.norm()`  | Vector/matrix norms             |


    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()