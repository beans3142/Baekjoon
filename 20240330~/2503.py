from sys import stdin
from itertools import permutations
input=stdin.readline

def fitcase(case):
    for fit in fits:
        strike=0
        ball=0
        nums=list(str(fit[0]))
        for digit in range(3):
            if nums[digit]==case[digit]:
                strike+=1
            elif nums[digit] in case:
                ball+=1
        if strike!=fit[1] or ball!=fit[2]:
            return False
    return True
    
n=int(input())
fits=[list(map(int,input().split())) for i in range(n)]
cases=list(permutations('123456789',3))
ans=0

for case in cases:
    ans+=fitcase(case)

print(ans)
