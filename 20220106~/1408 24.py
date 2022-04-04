nowtime=list(map(int,input().split(':')))
start=list(map(int,input().split(':')))
time_left=[]

for i in range(3):
    time_left.append(start[i]-nowtime[i])

for i in range(2):
    if time_left[-1-i]<0:
        time_left[-1-i]+=60
        time_left[-2-i]-=1

if time_left[0] < 0:
    time_left[0]+=24

print('{0:0>2}:{1:0>2}:{2:0>2}'.format(time_left[0],time_left[1],time_left[2]))

#https://www.acmicpc.net/problem/1408
