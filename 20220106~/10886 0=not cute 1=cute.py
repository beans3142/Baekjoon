n=int(input())
vote=[]
for i in range(n):
    vote.append(input())

if vote.count('1')> vote.count('0'):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

#https://www.acmicpc.net/problem/10102
