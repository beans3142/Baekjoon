from sys import *

input=stdin.readline

s=input().rstrip()
a=True

def div(w):
    global a
    m=len(w)//2
    if m==0:
        return
    for i in range(m):
        if w[i]==w[m-1-i]==w[m+len(w)%2+i]==w[-i-1]:
            continue
        a=False
    div(w[:m])

div(s)

if a:
    print('AKARAKA')
else:
    print('IPSELENTI')
