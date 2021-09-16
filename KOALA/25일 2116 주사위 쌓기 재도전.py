from sys import stdin
input=stdin.readline

n=int(input())
toplist=[[0,0,0,0,0,0]for i in range(n)]
sumlist=[[0,0,0,0,0,0]for i in range(n)]
floor=list(map(int,input().split()))
relation={0:5,1:3,2:4,3:1,4:2,5:0}
for idx,i in enumerate(floor):
    toplist[0][idx]=i
    for j in range(1,7):
        if j!=i and j!=floor[relation[idx]]:
            sumlist[0][idx]=max(sumlist[0][idx],j)
        

for height in range(1,n):
    floor=list(map(int,input().split()))
    for ver,i in enumerate(toplist[height-1]):
        for idx,j in enumerate(floor):
            if j==i:
                nexttop=floor[relation[idx]]
                for num in range(1,7):
                    if num!=j and num != nexttop:
                        sumlist[height][ver]=max(sumlist[height][ver],sumlist[height-1][ver]+num)
                toplist[height][ver]=nexttop                                
        

print(max(sumlist[-1]))
