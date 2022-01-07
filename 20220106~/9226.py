from sys import stdin
from collections import deque
input=stdin.readline

alphabet={chr(97+i):0 for i in range(26)}
for i in ['a','e','i','o','u']:
    alphabet[i]=1

while True:
    s=input().rstrip()
    if s=='#':
        break
    s=list(s)
    for i in range(len(s)):
        if alphabet[s[0]]:
            break
        s.append(s.pop(0))
    print(''.join(s)+'ay')


