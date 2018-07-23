'''
TASK:
=========
You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .
'''


def eval_polynomial(poly, val):
    xs = [ x.strip().replace('^','**') for x in poly.split('+') ]
    return sum( [eval(n.replace('x', str(val))) for n in xs] )


try:
    x, k = [int(x) for x in input().split()]
    p = input()
    poly = eval_polynomial(p, x)
    if poly == k:
        print(True)

    else:
        print(False)
except ValueError:
    print("Enter substitute Variable and output")
