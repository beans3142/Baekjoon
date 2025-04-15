from sys import stdin
input=stdin.readline

def check(row,col):
    if useCol&(1<<col) or useDiag&(1<<(row+col)) or useReversedDiag&(1<<((n-1)-row+col)):
        return False
    return True

def backTracking(row):
    global useCol,useDiag,useReversedDiag
    ans=0
    if row==n:
        return 1
    for col in range(n):
        if check(row,col):
            useCol=useCol|1<<col
            useDiag|=(1<<(row+col))
            useReversedDiag|=(1<<((n-1)-row+col))
            ans+=backTracking(row+1)
            useCol^=1<<col
            useDiag^=(1<<(row+col))
            useReversedDiag^=(1<<((n-1)-row+col))
    return ans

n=int(input())

useCol=0
useDiag=0
useReversedDiag=0

print(backTracking(0))
