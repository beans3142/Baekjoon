import sys
input = sys.stdin.readline

def getprob(n1, m1, n2, m2):
    tmp = 1.0
    for i in range(m1 + 1):
        tmp *= (n1 + 1 - i) / (n1 + n2 + 2 - i)

    ans = tmp
    for i in range(1, m2 + 1):
        tmp *= ((m1 + i) * (n2 + 2 - i) / ( i * (n1 + n2 + 2 - m1 - i) ))
        ans += tmp

    return ans

t = int(input())
res = []

for _ in range(t):
    n1, m1, n2, m2 = map(int, input().split())
    prob = getprob(n1, m1, n2, m2)
    res.append(f"{prob:.5f}")

print("\n".join(res))
