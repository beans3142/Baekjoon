from sys import stdin
input=stdin.readline


inf=float('inf')

def getdist(x1,y1,x2,y2):
    return (x2-x1)**2+(y2-y1)**2

def ccw(x1,y1,x2,y2,x3,y3): # 양수 반시계 음수 시계
    a=(x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
    if a>0:
        return 1
    else:
        return -1

def cov_hul():
    stack=[dots[0],dots[1]]

    for i in range(2,n):
        while len(stack)>=2:
            d2=stack.pop()
            if ccw(*stack[-1],*d2,*dots[i])>0:
                stack.append(d2)
                break
        stack.append(dots[i])
    return stack

if __name__=="__main__":
    dots=[]
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        dots.append([a,b])

    dots.sort(key=lambda x:(x[1],x[0]))
    arr=[]

    arr+=cov_hul()
    arr.pop()
    dots.reverse()

    arr+=cov_hul()
    arr.pop()
    
    le=len(arr)
    a=arr.index(min(arr))
    b=a+1
    c=arr.index(max(arr))
    d=c+1
    b%=le
    d%=le
    st=arr[a]
    ans=-1
    for i in range(le*2):
        dist=getdist(*arr[a],*arr[c])
        if dist>ans:
            ans=dist
            ansdot=(*arr[a],*arr[c])
        dx=arr[d][0]-arr[c][0]+arr[b][0]
        dy=arr[d][1]-arr[c][1]+arr[b][1]
        if ccw(*arr[a],*arr[b],dx,dy)>0:
            c+=1
            d+=1
            c%=le
            d%=le
        else:
            a+=1
            b+=1
            a%=le
            b%=le
            
    print(*ansdot)
