'''
def merge(l1,l2,l3):
    return [''.join(i) for i in zip(l1,l2,l3,l2,l1)]
    #l=[''.join(i) for i in list(zip(l1,l2,l3,l2,l1))]
    #return l

def star(x):
    x//=2
    if x==0:
        return '*'
    s=star(x)
    t=merge([' '*x]*x,[' '*x]*x,s)
    m=merge([' '*x]*x,s,[' '*x]*x)
    b=merge(s,s,s)
    return t + m + b

print('\n'.join(star(int(input()))))
'''
import math

s = ['  *   ', ' * *  ', '***** ']

def make_fractal(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = ("   " * shift + s[i] + "   " * shift)
        
n = int(input())
k = int(math.log(int(n / 3), 2))
for i in range(k):
    make_fractal(int(pow(2, i)))
for i in range(n):
    print(s[i])
