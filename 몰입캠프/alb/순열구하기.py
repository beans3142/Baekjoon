from itertools import permutations
n,r=map(int,input().split())
case=list(permutations(range(1,n+1),r))
for i in case:
    for j in i:
        print(chr(96+j),end='')
    print()
