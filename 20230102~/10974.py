import itertools as i
n=int(input())
for i in i.permutations(range(1,n+1),n):
    print(*i)
