import sys
input=sys.stdin.readline

arr={}
for i in range(97,123):
    arr[chr(i)]=i-96

r=31
m=1234567891

n=int(input())
strings=input().rstrip()
hashi=0
for i in range(n):
    hashi+=arr[strings[i]]*31**i
    
print(hashi)
