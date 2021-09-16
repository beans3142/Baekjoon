num=int(input())

for i in range(0,num):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    r=((x1-x2)**2+(y1-y2)**2)**0.5
    if x1==x2 and y1 == y2:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    elif r < r2 or r < r1:
        if abs(r2-r1) > r:
            print(0)
        elif abs(r2-r1) < r:
            print(2)
        else:
            print(1)      
    else:
        if r1 + r2 < r:
            print(0)
        elif r1 + r2 > r:
            print(2)
        else:
            print(1)
