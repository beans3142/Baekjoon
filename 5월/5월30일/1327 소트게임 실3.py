import sys
input=sys.stdin.readline

#n,k=map(int,input().split())
#arr=tuple(map(int,input().split()))
n,k=5,4
arr=(5,4,3,2,1)
temp={arr:0}
made=[arr]

if arr!=tuple(sorted(arr)):
    arr=tuple(sorted(arr))
else:
    print(0)
    exit()

for i in made:
    for j in range(n-k+1):
        s=i[:j]+tuple(reversed(i[j:j+k]))+i[j+k:]
        if s not in made:
            if s == arr:
                print(temp[i]+1)
                exit()
            temp[s]=temp[i]+1
            made.append(s)

print(-1)
