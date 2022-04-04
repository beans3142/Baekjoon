from sys import stdin
input=stdin.readline

n=int(input())
state=list(map(int,input().split()))

def nam(x):
    dif=x
    x-=1
    while x<n:
        state[x]=abs(state[x]-1)
        x+=dif

def nyu(x):
    left=x-1
    right=x-1
    state[x-1]=abs(state[x-1]-1)
    while -1<left:
        try:
            state[left]=abs(state[left]-1)
            state[right]=abs(state[right]-1)
            left-=1
            right+=1
            if state[left]!=state[right]:
                break
        except:
            break

for i in range(int(input())):
    sex,num=map(int,input().split())
    if sex==1:
        nam(num)
    else:
        nyu(num)

for i in range(n):
    print(state[i],end='\n' if i%20==19 else ' ')
