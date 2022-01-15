from sys import stdin
input=stdin.readline
no=1

while True:
    try:
        r,w,l=map(int,input().split())
        if (w**2+l**2)**0.5/2<=r:
            print(f'Pizza {no} fits on the table.')
        else:
            print(f'Pizza {no} does not fit on the table.')
        no+=1
    except:
        break
