from sys import stdin
input=stdin.readline


inf=float('inf')

def ccw(x1,y1,x2,y2,x3,y3):
    a=(x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
    if a>0:
        return 1
    if a==0:
        return 0
    else:
        return -1

def cov_hul():
    stack=[dots[0],dots[1]]

    for i in range(2,n):
        while len(stack)>=2:
            if ccw(*stack[-1],*stack[-2],*dots[i])>0:
                break
            stack.pop()
        stack.append(dots[i])
    return len(stack)

dots=[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    dots.append([a,b])

dots.sort(key=lambda x:(x[1],x[0]))
ans=-2

ans+=cov_hul()

dots.reverse()

ans+=cov_hul()

print(ans)
