from sys import stdin
input=stdin.readline


n,k=map(int,input().split())
k-=5
alphabet={chr(97+i):i for i in range(26)}
used={chr(97+i):0 for i in range(26)}
ans=0
mask={}

for i in range(n):
    word=set(input().rstrip())
    bit=['0']*26
    for j in word:
        bit[alphabet[j]]='1'
        used[j]=1
    bi=''.join(bit)
    try:
        mask[bi][0]+=1
    except:
        mask[bi]=[1,need]

for i in ['a','n','t','i','c']:
    used[i]=0

able=[i for i in used if used[i]==1]
vi=[0]*len(able)

def check(arr):
    global ans
    cnt=0
    for j in mask:
        same=0
        for i in arr:
            if j[alphabet[i]]=='1':
                same+=1
        if same==mask[j][1]:
            cnt+=mask[j][0]
    ans=max(cnt,ans)

def dfs(w,idx):
    if len(w)==k:
        check(w)
        return
    for i in range(idx,len(able)):
        if vi[i]==0:
            vi[i]=1
            dfs(w+able[i],idx+1)
            vi[i]=0

dfs('',0)
        
print(ans)
