def c(n,m):
    return p(n,m)//p(m,m)
    
def p(n,left):
    if n<2 or left==0:
        return 1
    return n*p(n-1,left-1)

n,m=map(int,input().split())
print(c(n,m))

'''
TC
기본적인 구현 0!은 1
in
0 0

out
1

in
2 2

out
1

in
5 0

out
1

구현 제대로 되어있나
in
29 14

out
77558760
'''
