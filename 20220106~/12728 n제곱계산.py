from sys import stdin
from math import sqrt
from decimal import Decimal
from fractions import Fraction
input=stdin.readline

def power(n):
    a=3+Fraction(5**0.5)
    ret = 1
    while n > 0:
        if n % 2 != 0:
            ret *= a
        a *= a
        ret%=1000
        n //= 2   
    return int(ret)
'''
for i in range(int(input())):
    print(f"Case #{i+1}: {str(power(int(input()))).zfill(3)}")
'''
cnt=0
if True:
    nums = [6, 28]
    numSet = set(nums)
    temp = 6 * nums[-1] - 4 * nums[-2]
    
    for _ in range(100):
        nums.append(temp)
        numSet.add(temp)
        temp = (6 * nums[-1] - 4 * nums[-2]) % 1000
    cycleList = nums[2:]
    for _ in range(2,100):
        n = _
        ans = None
        if n <= 2:
            ans = str(nums[n - 1] - 1)
        else:
            ans = str(cycleList[(n - 2) % len(cycleList) - 1] - 1)
        while len(ans) < 3:
            ans = "0" + ans
        if ans!= str(power(n)).zfill(3):
            ans = "Case #" + str(_ + 1) + ": " + ans
            cnt+=1
            print(ans)
    print(cnt)
