from itertools import permutations as p
n,m,*a=map(int,open(0).read().split())
print(*sorted(p(a,m)),sep="\n")
