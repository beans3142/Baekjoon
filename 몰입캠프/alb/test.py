#1 값을 채워넣어 주는 방법
# 5*5 배열을 7*7배열의 1~6위치에 넣어주기 위해 반복문을 이용해 준다.

arr=[[0 for i in range(7)] for j in range(7)]
arr2=[[*map(int,input().split())] for i in range(5)]

for i in range(5):
  for j in range(5):
    arr[1+i][1+j]=arr2[i][j]

for i in arr:
  print(i)

#2 배열을 붙여서 해결하는 방법
# 입력받은 값을 넣기 전에 이미 윗부분을 완성시켜 놓은 배열을 만들어준다.
# 입력받은 값들 좌우에 0을 붙여서 배열에 넣어주고
# 입력을 모두 마치면 밑부분을 붙여준다.

arr3=[[0]*7]+[[0]+list(map(int,input().split()))+[0] for i in range(5)]+[[0]*7]
for i in arr3:
  print(i)


'''
입력

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
