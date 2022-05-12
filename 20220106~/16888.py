from sys import stdin
input=stdin.readline

dp=[0,1,0,1,1]+[0]*10**6

for i in range(5,10**6+1):
    for j in range(1,int(i**0.5)+1):
        if dp[i-j**2]==0:
            dp[i]=1
            break
        
t=int(input())    
    
for i in range(t):
    if dp[int(input())]:
        print('koosaga')
    else:
        print('cubelover')
