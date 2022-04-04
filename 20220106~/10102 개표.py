v=int(input())
vote=input()
a=vote.count('A')
b=vote.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')

#https://www.acmicpc.net/problem/10102
