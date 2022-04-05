def mountain(n):
    if n==1:
        return '1'
    return mountain(n-1)+str(n)+mountain(n-1)

print(mountain(int(input())))

'''
1처리

in
1

out
1
'''
