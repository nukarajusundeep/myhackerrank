def print_rangoli(size):
    # your code goes here
    for i in range(0,size):
        print("--")

size = int(input())
try:
    if size > 27 and size < 0:
except ValueError:
    print("Value should not be greater than 26 or less than 0")

print_rangoli(size)