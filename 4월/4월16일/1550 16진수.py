#백준 1550 https://www.acmicpc.net/problem/1550

n=input()

'''
num=[str(i) for i in range(0,10)]
spell=['A','B','C','D','E','F']
m=0
sum=0

for i in range(0,len(n)):
    if n[i] in num:
        m=int(n[i])
    elif n[i] in spell:
        m=10+spell.index(n[i])
    sum+=m*16**(len(n)-i-1)

print(sum)
'''
