from sys import stdin
input=stdin.readline

n=int(input())
cnt=0
sol=[0]*(n+1)

def merge(n,m):
    le=0
    add=m
    while m:
        m//=10
        le+=1
    return n*(10**(le))+add

def check():
    global sol
    sik=[1]
    for i in range(1,n):
        if sol[i]=='.':
            sik.append(merge(sik.pop(),i+1))
        else:
            sik.append(i+1)

    s=sik[0]
    idx=1
    for i in range(1,n):
        if sol[i]=='.':
            continue
        elif sol[i]=='+':
            s+=sik[idx]
            idx+=1
        else:
            s-=sik[idx]
            idx+=1
    if s==0:
        return True
        
        

def solution(now):
    global cnt,sol
    if now==n:
        state=check()
        if state==True:
            cnt+=1
            if cnt<=20:
                print(1,end=' ')
                for i in range(2,n+1):
                    print(sol[i-1],i,end=' ')
                print()
        return
    sol[now]='+'
    solution(now+1)
    sol[now]='-'
    solution(now+1)
    sol[now]='.'
    solution(now+1)
    
solution(1)
print(cnt)
