import sys
input=sys.stdin.readline

n=int(input()) # 시도 횟수
deck=[]

for i in range(n):
    scan=input().rstrip().split()
    if len(scan)>1:
        if scan[0]=='push_front':
            deck.insert(0,int(scan[1]))
        else:
            deck.append(int(scan[1]))
    else:
        scan=scan[0]
        if scan=='front':
            if deck:
                print(deck[0])
            else:
                print(-1)
        elif scan=='back':
            if deck:
                print(deck[-1])
            else:
                print(-1)
        elif scan=='size':
            print(len(deck))
        elif scan=='empty':
            if len(deck)==0:
                print(1)
            else:
                print(0)
        elif scan=='pop_front':
            if len(deck)==0:
                print(-1)
            else:
                print(deck.pop(0))
        else:
            if len(deck)==0:
                print(-1)
            else:
                print(deck.pop(-1))
