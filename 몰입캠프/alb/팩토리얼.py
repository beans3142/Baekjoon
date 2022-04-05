def fac(n):
    if n<2:
        return 1
    return n*fac(n-1)

print(fac(int(input())))

# 재귀든 메모이제이션이든 하기만 하면 됨.

'''
TC

0과 1 처리
in
0

out
1

in
1

out
1

in
10

out
3628800
'''
