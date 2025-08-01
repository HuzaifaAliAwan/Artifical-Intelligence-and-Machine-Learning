# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 20. Print the Fibonacci sequence up to n terms.

def get_fabonacci_seq(num):
    sequence = []
    a,b=0,1
    for _ in range(num):
        sequence.append(a)
        a,b = b,a+b
    return sequence
        
def main():
    try:
        num = int(input('Enter number : '))
        print(f'Fabonacci : {get_fabonacci_seq(num)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()