n=16
t=16
m=2
p=2



def change(n,m):
    s=''
    while n:
        s+=hex(n%m)[-1]
        n//=m
    return s[::-1] if s else '0'
        

def solution(n, t, m, p):
    enoughLongString=''
    idx=0
    stack=0
    nowstr=change(0,n)
    nownum=1
    answer = ''
    while len(answer)<t:
        if stack%m==p-1:
            answer+=nowstr[idx]
        idx+=1
        stack+=1
        if len(nowstr)==idx:
            idx=0
            nowstr=change(nownum,n)
            nownum+=1
            
            
    return answer.upper()

print(solution(n,t,m,p))
