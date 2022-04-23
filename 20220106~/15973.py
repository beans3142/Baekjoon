from sys import stdin
input=stdin.readline

def cia(rect1, rect2):
        
    x1, y1 = rect1[0], rect1[1] 
    x2, y2 = rect1[2], rect1[3]
    x3, y3 = rect2[0], rect2[1] 
    x4, y4 = rect2[2], rect2[3]

    if x2 < x3:
        return "NULL"

    if x1 > x4:
        return "NULL"

    if  y2 < y3:
        return "NULL"

    if  y1 > y4:
        return "NULL"

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

first=list(map(int,input().split()))
second=list(map(int,input().split()))
print(cia(first,second))
