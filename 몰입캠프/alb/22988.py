from sys import stdin
input=stdin.readline

'''
이걸 어떻게든 처리해야 하는데 ㅋㅋㅋ
4 13
1 2 11 12

좌우 투 포인터?

6 13
1 2 3 10 11 12
'''

def check(a,b):
    if a+b+x//2<x:
        return False
    return True

n,x=map(int,input().split())
arr=sorted(map(int,input().split()))
ans=0
while arr[-1]>=x:
    arr.pop()
    ans+=1

l,r=0,len(arr)-1
cr=0
ch=[]
'''
while l<r:
    if check(arr[l],arr[r]):
        ans+=1
        l+=1
        r-=1
    elif cr<len(ch) and check(arr[l],ch[cr]):
        ans+=1
        cr+=1
        l+=1
    else:
        ch.append(arr[l]+arr[l+1]+x//2)
        l+=2

'''
while l<r:
    if arr[r]>x//2:
        
if l==r and cr<len(ch) and check(arr[l],ch[cr]):
    ans+=1
print(ans)
