n=int(input())
s=input()
print(sum([ord(i)-ord('A') for i in s])+n)
