from sys import stdin

input=stdin.readline

presum=[1 for i in range(1000001)]
presum[0]=0

for i in range(2,1000001):
    presum[i]+=i
    for j in range(i+i,1000001,i):
        presum[j]+=i

for j in range(1,1000001):
    presum[j]=presum[j]+presum[j-1]

for i in range(int(input())):
    n=int(input())
    print(presum[n])
