from sys import stdin
input=stdin.readline
x,k=map(int,input().split())
x=bin(x)[2:][::-1]
k=bin(k)[2:][::-1]
idx=0
k_idx=0
ans=[]
while idx<len(x) and k_idx<len(k):
    if x[idx]=='1':
        ans.append(0)
    else:
        ans.append(int(k[k_idx]))
        k_idx+=1
    idx+=1
while k_idx<len(k):
    ans.append(int(k[k_idx]))
    k_idx+=1

num=0
for i in range(len(ans)):
    if ans[i]:
        num+=2**i
print(num)
