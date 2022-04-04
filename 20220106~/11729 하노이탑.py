# 가져온 코드

n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)

#

n=int(input())

move=1
for i in range(n-1):
    move=move*2+1

pat=[[1,3],[1,2],[3,2],[1,3],[2,1],[2,3]]
def hano(x):
    if x == move:
        return 0
    else:
        print(pat[x%6][0],pat[x%6][1])
        return hano(x+1)

print(move)

hano(0)



