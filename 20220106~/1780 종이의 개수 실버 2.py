import sys

input=sys.stdin.readline
n=int(input())
m=n
po=0
gaesu={-1:0,0:0,1:0}

while m!=1:
    m//=3
    po+=1
    
paper=[list(map(int,input().split())) for i in range(n)]

def div(l,x):
    if len(l)==1:
        gaesu[l[0][0]]+=1
        return
    is_same=True
    if len(set(l[x//2]))==1:
        for i in range(1,x//2+1):
            if l[x//2] != l[x//2-i] or l[x//2] != l[x//2+i]:
                is_same=False
                break
    else:
        is_same=False
    if not is_same:
        nl=[[],[],[]]
        for h in range(x):
            for w in range(3):
                nl[w]+=[l[h][x//3*w:x//3*(w+1)]]
            if (h+1)%(x//3)==0:
                div(nl[0],x//3)
                div(nl[1],x//3)
                div(nl[2],x//3)
                nl=[[],[],[]]
    else:
        gaesu[l[0][0]]+=1
        
div(paper,n)

print(gaesu[-1],gaesu[0],gaesu[1],sep='\n')
