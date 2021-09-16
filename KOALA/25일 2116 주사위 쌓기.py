from sys import stdin
input=stdin.readline

n=int(input())
stack=[]
mx=0

for i in range(n):
    dice=list(map(int,input().split()))
    pair=[[dice[1],dice[3]],[dice[0],dice[5]],[dice[2],dice[4]]]
    stack.append(pair)

for floor in stack[0]:
    line=[]
    for _ in stack[0]:
        if _!= floor:
            line+=_
    for j in range(2):
        print(1)
        s=max(line)
        top=floor[j]
        appendlist=[s]
        toplist=[top]
        for i in range(1,n):
            line=[]
            for side in stack[i]:
                if top in side:
                    for l in range(2):
                        if side[l]!=top:
                            nexttop=side[l]
                else:
                    line+=side
            bottom=top
            top=nexttop
            toplist.append(top)
            s+=max(line)
            appendlist.append(max(line))
        if mx<s:
            mx=max(s,mx)
            lasttop=nexttop
            lastappendlist=appendlist
            lasttoplist=toplist

print(mx)
