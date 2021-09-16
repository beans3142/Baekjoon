import sys
input=sys.stdin.readline

n=int(input())
cards=list(map(int,input().split()))
deck={}
for card in cards:
    if card not in deck:
        deck[card]=1
    else:
        deck[card]+=1
        
m=int(input())
find_card=list(map(int,input().split()))

for i in range(m):
    if find_card[i] in deck:
        print(deck[find_card[i]],end=' ')
    else:
        print(0,end=' ')
