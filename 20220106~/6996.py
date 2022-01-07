from sys import stdin
input=stdin.readline

n=int(input())
for i in range(n):
    s1,s2=input().rstrip().split()
    if sorted(s1)==sorted(s2):
        print(f'{s1} & {s2} are anagrams.')
    else:
        print(f'{s1} & {s2} are NOT anagrams.')
