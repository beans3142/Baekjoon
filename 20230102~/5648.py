from sys import stdin
input=stdin.readline

arr=[]
fst=input().rstrip().split()
le=int(fst.pop(0))
arr+=list(map(lambda x:int(x[::-1]),fst))
while len(arr)<le:
    arr+=list(map(lambda x:int(x[::-1]),input().split()))
print(*sorted(arr),sep='\n')
