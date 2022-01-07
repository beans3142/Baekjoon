from sys import stdin
input=stdin.readline

nums=[]
for i in range(7):
    n=int(input())
    if n%2==1:
        nums.append(n)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
