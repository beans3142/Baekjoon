from sys import stdin

n=int(input())
row=[0]*n
vi=[0]*n
ans=0

def bt(nowline):
    global ans
    if nowline==n:
        ans+=1
        return
    for i in range(n):
        if vi[i]==0:
            row[nowline]=i
            able=True
            for j in range(nowline):
                if row[j]!=-1 and abs(row[nowline]-row[j])==abs(nowline-j):
                    able=False
                    break
            if able:
                vi[i]=1
                bt(nowline+1)
                vi[i]=0


            
bt(0)
print(ans)
