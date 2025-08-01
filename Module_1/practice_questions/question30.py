# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 30. Check if two strings are anagrams.

import string

def get_all_letters():
    return string.ascii_lowercase

def check_anagram(str1, str2):
    letters = get_all_letters()
    
    for letter in letters:
        if str1.count(letter) != str2.count(letter):
            return False
    return True

def main():
    try:
        str1 = input('Enter string 1 : ').strip()
        str2 = input('Enter string 2 : ').strip()
        print('Anagram' if check_anagram(str1, str2) else 'Not Anagram')

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()