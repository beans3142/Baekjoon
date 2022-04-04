from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())

wordlist=[deque(input().rstrip()) for i in range(n)]
cnt=0

for i in wordlist:
    word=i
    cnt+=1
    wordlist.remove(word)
    for j in range(len(i)):
        word.append(word.popleft())
        if word in wordlist:
            wordlist.remove(word)

print(cnt)
