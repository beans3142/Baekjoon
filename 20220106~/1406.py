from sys import stdin
input=stdin.readline

class ll:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

    def remove(self):
        global le
        if (self.left)==None:
            return False
        le-=1
        self.left=(self.left).left
        if self.left==None:
            return True
        (self.left).right=val
        return False




s=list(input().rstrip())

arr=[ll(i,None,None) for i in s]

le=len(s)

for i in range(len(s)-1):
    arr[i].right=arr[i+1]
    arr[-i-1].left=arr[-i-2]

front=ll(None,None,arr[0])
rear=ll(None,arr[-1],None)
arr[0].left=front
arr[-1].right=rear
now=rear
m=int(input())
for i in range(m):
    order=input().split()
    if order[0]=='B':
        if (now.left)==None or now.left.left==None:
            continue
        else:
            le-=1
            now.left=(now.left).left
            now.left.right=now
    if order[0]=='P':
        if now==front:
            new=ll(order[1],now,now.right)
            now.right.left=new
            now.right=new
        else:
            new=ll(order[1],now.left,now)
            now.left.right=new
            now.left=new
        le+=1
    if order[0]=='L':
        if now!=front:
            now=now.left
    if order[0]=='D':
        if now!=rear:
            now=now.right
        
k=front

for i in range(le):
    print(front.right.val,end='')
    front=front.right
