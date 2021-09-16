from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
k-=5
alphabet={'b': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'j': 6,\
          'k': 7, 'l': 8, 'm': 9, 'o': 10, 'p': 11, 'q': 12, 'r': 13,\
          's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20,\
          'a':-1,'n':-1,'t':-1,'c':-1,'i':-1}

ans=0
mask={}
able={}
mx_len=0

for i in range(n):
    word=set(input().rstrip())
    bi=0
    for i in word:
        if alphabet[i]!=-1:
            bi+=2**alphabet[i]
            able[i]=1
    try:
        mask[bi]+=1
    except:
        mask[bi]=1

able=list(able)
vi=[0]*len(able)

def check(len_k_bin):
    global ans
    cnt=0
    for j in mask:
        if j&len_k_bin==j:
            cnt+=mask[j]
    ans=max(cnt,ans)


def dfs(w,idx,recur):
    if recur==k:
        check(w)
        return ans
    for i in range(idx,len(able)):
        if vi[i]==0:
            vi[i]=1
            dfs(w+2**alphabet[able[i]],i+1,recur+1)
            vi[i]=0

dfs(0,0,0)
print(n if len(able)<k else ans)
