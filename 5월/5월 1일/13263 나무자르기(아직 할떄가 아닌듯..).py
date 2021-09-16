#https://www.acmicpc.net/problem/13263

n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
wood={}
cost={}
cut_wood=[]
total_cost=[]
dp=[0]*n

for i,height in enumerate(a):
    wood[i+1]=height

for i,c in enumerate(b):
    cost[i+1]=c

def cut(n):
    wood[n]

for i in range(1,n): 
    dp[i]=min(b[j]*a[i]+dp[j])
'''
def getX(f,g):
    return (f[1]-g[1])//(g[0]-f[0])
 
def insert(x):
    k.append(x)
    while len(k)>2 and getX(k[-3], k[-2]) > getX(k[-2], k[-1]):
        k.pop(-2)
 
def bs(x):
    # print(k)
    l = 0
    r = len(k) - 1
 
    while l<r:
        mid = (l+r)//2
        if getX(k[mid], k[mid+1]) <= x:
            l = mid+1
        else:
            r = mid
    return k[l][0] * x + k[l][1]
 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0] * n
 
k = [(b[0], 0)]
for i in range(1, n):
    dp[i] = bs(a[i])
    insert((b[i], dp[i]))
print(dp[n-1])
'''
