# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

#  6. Swap two variables without a temporary variable.

def swap(v1,v2):
    v1, v2 = v2, v1
    return v1, v2

def main():
    try:
        var1 = input("Enter first variable value : ")
        var2 = input("Enter second variable value : ")
        
        var1 ,var2 = swap(var1, var2)

        print(f'Value of variable one : {var1}')
        print(f'Value of variable two : {var2}')
    except:
        print('Invalid Entry, Try again..!')

if __name__ == '__main__':
    main()