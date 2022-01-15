from sys import stdin
input=stdin.readline
n=int(input())
pat=input().rstrip().split('*')
for i in range(n):
    s=input().rstrip()
    if len(s)>=len(pat[0])+len(pat[1]) and pat[0]==''.join(s[:len(pat[0])]) and pat[-1]==s[-len(pat[1]):]:
        print("DA")
    else:
        print("NE")
