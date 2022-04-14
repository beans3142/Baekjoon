from sys import stdin
input=stdin.readline

vi=[[0 for i in range(5)] for j in range(5)]

def bt(place,cnt,cnt_a):
    global ans
    if cnt==7:
        if cnt_a>=4:
            ans+=1
        return
    for x,y in place:
        for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if -1<ny<5 and -1<nx<5:
                if vi[ny][nx]==0:
                    vi[ny][nx]=1
                    bt(place+[[nx,ny]],cnt+1,cnt_a+1 if arr[ny][nx]=='A' else cnt_a)
                    vi[ny][nx]=0

arr=[input().rstrip() for i in range(5)]
ans=0

for i in range(5):
    for j in range(5):
        vi[i][j]=1
        bt([[j,i]],1,0 if arr[i][j]=='B' else 1)
        vi[i][j]=0

print(ans)
