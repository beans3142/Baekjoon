def merge(r1,r2):
    a=[''.join(x) for x in zip(r1,r2,r1)]
    return a

def star(n):
    if n==1:
        return ['*']
    n//=3
    x=star(n)
    top_bottom=merge(x,x)
    middle=merge(x,[' '*n]*n)
    return top_bottom + middle + top_bottom

print('\n'.join(star(3**int(input()))))
'''
a=['*','*']
b=['*',' ']
c=[' ','*']

def sqrt(l1,l2,l3):
    print(list(zip(l1,l2,l3)))
    for i in zip(l1,l2,l3):
        print(''.join(i))

sqrt(a,b,c)
'''
