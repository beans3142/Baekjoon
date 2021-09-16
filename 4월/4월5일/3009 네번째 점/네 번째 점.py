x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

x_all=[x1,x2,x3] ; y_all=[y1,y2,y3]

for x in x_all:
    if x_all.count(x)==1:
        x4=x

for y in y_all:
    if y_all.count(y)==1:
        y4=y

print(x4,y4)
