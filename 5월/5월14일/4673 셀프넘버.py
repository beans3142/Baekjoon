#https://www.acmicpc.net/problem/4673

nl=list(range(1,10001))

def self_num(n):
    if n>10000:
        return 0
    for i in str(n):
        n+=int(i)
    if n in nl:
        nl.remove(n)

for i in range(1,10001):
    self_num(i)

for i in nl:
    print(i)
