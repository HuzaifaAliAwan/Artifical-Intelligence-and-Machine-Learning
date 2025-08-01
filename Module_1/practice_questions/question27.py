# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# 27. Count vowels in a user-input string.

def vowels_count(string):
    string.lower()
    vowels = 'aeiou'
    total_vowels_count = 0
    for vowel in vowels:
        total_vowels_count += string.count(vowel)
    return total_vowels_count


def main():
    try:
        data = input('Enter a sentence : ')
        print(f'Vowels in entered string : {vowels_count(data)}')
    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()