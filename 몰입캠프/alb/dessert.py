from sys import stdin
input=stdin.readline

n=int(input())
cnt=0

def check(sol,sik):
    SUM=sik[0]
    for i in range(len(sik)//2):
        if sik[2*i+1]=='+':
            SUM+=sik[2*i+2]
        else:
            SUM-=sik[2*i+2]
    if SUM==0:
        return True
    return False

def solution(now,sol,sik):
    global cnt
    if now==n:
        state=check(sol,sik)
        if state==True:
            cnt+=1
            if cnt<=20:
                print(sol)
            return True
        return False
            
    if solution(now+1,sol+' + '+str(now+1),sik+['+',now+1]):
        return
    if solution(now+1,sol+' - '+str(now+1),sik+['-',now+1]):
        return
    sik[-1]=int(str(sik[-1])+str(now+1))
    solution(now+1,sol+' . '+str(now+1),sik)
    
solution(1,'1',[1])
print(cnt)
