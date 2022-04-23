from random import *

while True:
    a=list(map(int,input().split()))
    print(*a)
    a[2]=a[0]+a[2]
    a[3]=a[1]+a[3]
    b=list(map(int,input().split()))
    print(*b)
    b[2]=b[0]+b[2]
    b[3]=b[1]+b[3]

    def cia(rect1, rect2):
        
        x1, y1 = rect1[0], rect1[1] 
        x2, y2 = rect1[2], rect1[3]
        x3, y3 = rect2[0], rect2[1] 
        x4, y4 = rect2[2], rect2[3]

        if x2 < x3:
            return "Null"

        if x1 > x4:
            return "Null"

        if  y2 < y3:
            return "Null"

        if  y1 > y4:
            return "Null"

        left_up_x = max(x1, x3)
        left_up_y = max(y1, y3)
        right_down_x = min(x2, x4)
        right_down_y = min(y2, y4)

        width = right_down_x - left_up_x
        height =  right_down_y - left_up_y

        if height==0 and width==0:
            return "POINT"
        elif height==0 or width==0:
            return "LINE"
        return "FACE"

    print(*cia(a,b))
    #print()
