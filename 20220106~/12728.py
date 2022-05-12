from sys import stdin
input=stdin.readline


nums=[6, 28]
tmp=6*nums[-1]-4*nums[-2]
    
for _ in range(100):
    nums.append(tmp)
    tmp=(6*nums[-1]-4*nums[-2])%1000

cycle = nums[2:]
t=int(input())

for _ in range(t):
    n=int(input())
    if n<=2:
        ans=nums[n - 1] - 1
    else:
        ans=cycle[(n-2)%len(cycle)-1]-1

    print(f'Case #{_+1}: {ans:03d}')
