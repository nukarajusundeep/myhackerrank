'''
### [Challenge Name: String Formatting](/challenges/python-string-formatting)


Given an integer, $n$, print the following values for each integer $i$ from $1$ to $n$:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line *in the order specified above* for each $i$ from $1$ to $n$. Each value should be space-padded to match the width of the *binary* value of $n$.
'''


def print_formatted(number):
    # your code goes here
    i = 1
    width = len(bin(number)[2:])
    while i < number+1:
        print(' '.join(map(lambda f: f.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)