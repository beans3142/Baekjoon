## template
## deque로 구현 가능할거 같다
## a b c d 순차적으로 넣었을대 bacd조합이 가능하면 명령어들 출력 아니면 impossible
## abcd는 bacd의 정렬 문자이기 때문에 정렬을 시켜준 후 순차적으로 앞의 문자를 꺼내준 후 스택에 쌓아 준다.
## stack제일 마지막값과 현재 문자와 같다면 pop 아니면 계속 푸쉬 
## 최종적으로 stack이 비워져있으면 통과 아니면 impossible

from collections import deque
x = list(input())
y = x[:]
y.sort()
x = deque(x)
y = deque(y)
stack = []
command = []
while len(y)>=0:
  if len(stack)>0 and stack[len(stack)-1] == x[0]:
    stack.pop()
    x.popleft()
    command.append('pop')
    if len(y) ==0:
      break
  else:
    stack.append(y.popleft())  
    command.append('push')
if len(stack)==0:
  for i in command:
    print(i)
else:
  print('impossible')
