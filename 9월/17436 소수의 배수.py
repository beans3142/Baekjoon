from sys import stdin

n,m=map(int,input().split())
prime=list(map(int,input().split()))

vi=[0]*n
ans=0

def bt(idx,nums,depth):
    global ans
    for i in range(idx,n):
        if vi[i]==0:
            vi[i]=1
            bt(i,nums*prime[i],depth+1)
            val=m//(nums*prime[i])
            if depth%2==0:
                val=-val
            ans+=val
            vi[i]=0
bt(0,1,1)
print(ans)
