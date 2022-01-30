from itertools import permutations

n=tuple(input())
case=list(permutations(sorted(n)))

for i in case:
    if n<i:
        print(''.join(i))
        exit()

print(0)
