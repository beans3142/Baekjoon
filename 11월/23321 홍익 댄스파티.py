from sys import stdin
input=stdin.readline

arr=[list(input().rstrip()) for i in range(5)]
for i in range(len(arr[0])):
    if arr[2][i]=='m':
        arr[0][i]='o'
        arr[1][i]='w'
        arr[2][i]='l'
        arr[3][i]='n'
        arr[4][i]='.'
    elif arr[2][i]=='l':
        arr[0][i]='.'
        arr[1][i]='o'
        arr[2][i]='m'
        arr[3][i]='l'
        arr[4][i]='n'

for i in arr:
    print(''.join(i))
