from sys import stdin
input=stdin.readline

n=int(input())
mx=0
daepyo=''
order=['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
for i in range(9):
    clubmember=list(map(int,input().split()))
    nowmx=max(clubmember)
    if nowmx>mx:
        mx=nowmx
        daepyo=order[i]

print(daepyo)
