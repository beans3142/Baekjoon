from sys import stdin
input=stdin.readline

s_len=int(input())
s=input().rstrip()
two=s.count("2")
e=s.count("e")
if two>e:
    print("2")
elif two<e:
    print("e")
else:
    print('yee')
