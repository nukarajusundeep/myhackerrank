import string

def first_half(size):
    mid = size - 1
    for i in range(size - 1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

def second_half(size):
    mid = size - 1
    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))
def rangoli(size):
    first_half(size)
    second_half(size)


if __name__ == '__main__':
    size = int(input("Enter the size of rangoli: "))
    rangoli(size)