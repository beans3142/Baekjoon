from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
word=[]
for i in range(n):
    r=0
    s=set(input().rstrip())
    for j in s:
        r|=1<<(ord(j)-97)
    word.append(r)

now=0
for i in range(m):
    t,w=input().rstrip().split()
    if t=='1':
        now|=1<<(ord(w)-97)
    else:
        now^=1<<(ord(w)-97)
    cnt=0
    for s in word:
        if s&now:
            cnt+=1
    print(n-cnt)
