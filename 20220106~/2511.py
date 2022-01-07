from sys import stdin
input=stdin.readline

a=list(map(int,input().split()))
b=list(map(int,input().split()))
last_win='D'
scorea=0
scoreb=0

for i in range(10):
    if a[i]>b[i]:
        scorea+=3
        last_win='A'
    elif a[i]<b[i]:
        scoreb+=3
        last_win='B'
    else:
        scorea+=1
        scoreb+=1

print(scorea,scoreb)
if scorea>scoreb:
    print('A')
elif scorea<scoreb:
    print('B')
else:
    print(last_win)
