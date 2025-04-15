from collections import defaultdict
from bisect import *
n=int(input())
arr=sorted(map(int,input().split()))
dd=defaultdict(int)
for i in arr:
    dd[i]+=1
first=arr[-1]
second=arr[-2]
third=arr[-3]
s=sum(arr)
ans=0

# 해결법은 bisect를 활용하는 것,
# 합이 s, 가장 큰 원소 first, 지울 원소 i,j에 대해 i를 정하게 되면 나머지 값을 알 수 있다.
# 식은 s-first-i-j=first를 만족하는 i,j를 찾는 것인데, i를 정하게 되면 j에 대한 식으로 바꿀 수 있다.
# j=s-2*first-i 이렇게 식을 쓰고, case를 3개로 나눌 수 있다.
# case 1 마지막 원소를 고정하고, n-1개 원소들 중 i,j를 정하는 경우, j=s-2*first-i
# case 2 마지막 원소는 무조건 지우고, n-1개 원소들 중 i를 정하는 경우, 두번째로 큰 원소를 second라 했을 때 second=s-first-i-second -> i=s-first-second*2 를 만족하는 i
# case 3 맨 뒤 원소 2개를 지우는 경우, 이 경우는 하나라서 간단하게 세주면 된다. 세번째로 큰 원소를 third라 했을 때 third=s-first-second-third -> third*2==s-first-second

# case1의 경우
# 맨 뒤에는 고정, n-1개에 대해 2개를 지우는 경우
# 합이 s, 맨뒤(가장 큰 원소)가 first, 지울 원소 2개가 first인 경우
# s-first 가장큰 원소를 제외한 나머지 원소
# s-first-i-j 가장 큰 원소를 제외하고 2개 원소를 지운 경우
# s-first-i-j = first 가장큰 원소와 가장 큰 원소를 제외하고 2개 원소를 지운 경우가 같은 경우
# i를 정했다 가장했을 때 j를 찾으면 된다.
# j=s-2*first-i 이므로 j를 찾으면 된다.

# 신경써야 할 것들은 다음과 같다, i=j인 경우와 i,j와 j,i 순서가 달라도 하나로 세야 하는 것이다.

# i,j와 j,i를 해결하기 위해, j>=i조건을 넣어줬다. 이를 통해 순서가 달라도 중복해서 세지 않는다.
# i=j인 경우가 살짝 복잡한데
# 나는 j>=i조건을 이용해 bisect_left에 max를 함께 넣어서 해결했다.
# j를 bisect_left 한 결과는 3가지이다.
# 1. i의 index보다 작은 경우
# 2. i의 index와 같은 경우
# 3. i의 index보다 큰 경우
# 1의 경우, i!=j면 j>=i에 의해 걸러지게 되고,
# i==j인 경우 발생할 수 있다. 3 3 3 이렇게 있다면 두번째 3을 bisect 한 경우 bisect의 결과가 i의 index보다 작아진다.
# 이렇게 된 경우 중복하게 세게 될 수 있으므로, max(i+1,bisect_left)로 해결해줄 수 있다. i+1 자기 자신 포함 하지 않고, 자기보다 큰 경우
# 2의 경우도 위를 통해 자기자신보다 무조건 큰 인덱스를 활용하도록 해줬으므로 문제가 없다.
# 3의 경우 bisect의 결과가 항상 i+1보다 크기 때문에 문제가 없다.

case1=arr[:-1]
for idx in range(n-1):
    i=case1[idx]
    j=s-2*first-i
    if j<i:continue
    cnt=bisect_right(case1,j)-max(idx+1,bisect_left(case1,j))
    ans+=cnt

# case2의 경우
case2=arr[:-2]
for i in case2:
    if i==s-first-2*second:
        ans+=1

# case3의 경우
if third*2==s-first-second:
    ans+=1

print(ans)