import sys
input=sys.stdin.readline

s={}

for i in range(1,21):
    s[str(i)]=0

for i in range(int(input())):
    try:
        order=input().rstrip().split()
        o,x=order[0],order[1]
        if o == 'add':
            s[x]=1
        elif o =='remove':
            s[x]=0
        elif o=='check':
            print(s[x])
        else:
            if s[x]:
                s[x]=0
            else:
                s[x]=1
    except IndexError:
        if order[0]=='all':
            for i in s:
                s[i]=1
        else:
            for i in s:
                s[i]=0

# 시간초과 나는 코드
'''
s=[]
n=int(input())

for i in range(n):
    try:
        order=input().rstrip().split()
        o,x=order[0],order[1]
        if o == 'add':
            if x not in s:
                s.append(x)
        elif o =='remove':
            if x in s:
                s.remove(x)
        elif o=='check':
            if x in s:
                print(1)
            else:
                print(0)
        else:
            if x not in s:
                s.append(x)
            else:
                s.remove(x)        
    except IndexError:
        if order[0]=='all':
            s=[str(i) for i in range(1,21)]
        else:
            s=[]
'''
