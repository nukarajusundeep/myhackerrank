'''Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123'''


def echo_seq(a):
    for i in range(1, a+1):
        print('%s' % i, end="")


if __name__ == '__main__':
    n = int(input())
    echo_seq(n)

