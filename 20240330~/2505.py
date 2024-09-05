from sys import stdin
input=stdin.readline

def check():
    points=[]
    for i in range(1,n+2):
        if abs(arr[i]-arr[i-1])>1:
            points.append(i-1)
            points.append(i)
    return points

def bt(dep):
    case=check()
    if not case:
        for i in ans:
            print(*i)
        for i in range(2-len(ans)):
            print(1,1)
        exit()
    if dep==2:
        return
    for ii in range(len(case)):
        for jj in range(ii+1,len(case)):
            i=case[ii]
            j=case[jj]
            for k in range((j-i)//2+1):
                arr[i+k],arr[j-k]=arr[j-k],arr[i+k]
            ans.append((i,j))
            bt(dep+1)
            for k in range((j-i)//2+1):
                arr[i+k],arr[j-k]=arr[j-k],arr[i+k]
            ans.pop()

n=int(input())
arr=[0]+list(map(int,input().split()))+[n+1]
ans=[]
bt(0)
