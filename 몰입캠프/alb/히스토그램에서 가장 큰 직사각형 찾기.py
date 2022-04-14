from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))+[0]
    
tmp=[0]
area=0

for i,h in enumerate(arr):
    while tmp and arr[tmp[-1]]>h:
        height=arr[tmp.pop()]
        if tmp:
            width=i-tmp[-1]-1
        else:
            width=i
        if area<width*height:
            area=width*height
    tmp.append(i)

print(area)
