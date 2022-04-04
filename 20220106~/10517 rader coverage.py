from sys import *
input=stdin.readline

t=int(input())

for i in range(t):
    #x1,x2,x3,y1,y2,y3=map(int,input().split())
    #x1,y1,x2,y2,x3,y3=map(int,input().split())
    ax,ay,bx,by,cx,cy=map(int,input().split())
    '''
    x=-((x2**2-x1**2+y2**2-y1**2)*(y3-y2)-(x2**2-x3**2+y2**2-y3**2)*(y1-y2))\
       /(2*(x1-x2)*(y3-y2)-2*(x3-x2)*(y1-y2))


    x1,y1=y1,x1
    x2,y2=y2,x2
    x3,y3=y3,x3
    y=-((x2**2-x1**2+y2**2-y1**2)*(y3-y2)-(x2**2-x3**2+y2**2-y3**2)*(y1-y2))\
       /(2*(x1-x2)*(y3-y2)-2*(x3-x2)*(y1-y2))
    print('Case #%d: %0.2f %0.2f'%(i+1,round(x,2),round(y,2)))
'''
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    
    print('Case #%d: %0.2f %0.2f'%(i+1,round(ux,2),round(uy,2)))
