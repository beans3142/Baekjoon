n=int(input())

arr=list(map(int,input().split()))
s_arr=sorted(arr)
zipped={}
same=0
for i in range(n):
    try:
        zipped[s_arr[i]]
        same+=1
    except KeyError:
        zipped[s_arr[i]]=i-same

for i in arr:
    print(zipped[i],end=' ')
