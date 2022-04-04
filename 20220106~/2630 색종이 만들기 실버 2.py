import sys

input=sys.stdin.readline
n=int(input())
gaesu=[0,0]

paper=[list(map(int,input().split())) for i in range(n)]

def div(l,x):
    if len(l)==1:
        gaesu[l[0][0]]+=1
        return
    is_same=True
    if len(set(l[0]))==1:
        for i in range(1,x):
            if l[0] != l[i]:
                is_same=False
                break
    else:
        is_same=False
    if not is_same:
        nl=[[],[],[]]
        for h in range(x):
            for w in range(2):
                nl[w]+=[l[h][x//2*w:x//2*(w+1)]]
            if (h+1)%(x//2)==0:
                div(nl[0],x//2)
                div(nl[1],x//2)
                nl=[[],[],[]]
    else:
        gaesu[l[0][0]]+=1
        
div(paper,n)

print(gaesu[0],gaesu[1],sep='\n')
