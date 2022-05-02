x,y,w,s=map(int,input().split())
if w<=s//2:
    print((x+y)*w)
else:
    base=min(x,y)*s
    add=min((max(x,y)-min(x,y))*w,(max(x,y)-min(x,y))//2*2*min(s,w)+(max(x,y)-min(x,y))%2*w)
    print(base+add)
