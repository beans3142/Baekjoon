x,y=map(int,input().split())
l1=y-x
k=0
l2=0
while l2<l1:
  k+=1
  l2+=(k+1)//2
print(k)

'''
TC

in
0 2147483647

out
92681

거리가 n^2 + n일 때 +1을 더해서 출력하는 오류
in
0 6

out
4

in
0 7

out
5

in
1 8

out
5
'''
