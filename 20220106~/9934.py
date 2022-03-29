from sys import stdin
input=stdin.readline

k=int(input())
order=list(map(int,input().split()))

line=[(len(order)//2,0,len(order))]
while True:
    nextline=[]
    for i,mn,mx in line:
        print(order[i],end=' ')
        nextline.append(((i+mn)//2,mn,i))
        nextline.append(((i+mx)//2,i,mx))
    print()
    line=nextline
    if len(line)==2**k:
        break
        
