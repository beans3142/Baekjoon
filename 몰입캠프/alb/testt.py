## template

#####################################################
#(1) 스택의 맨 위에 여느 괄호가 있는 경우
# 스택에서 맨 위에 있는 여느괄호를 pop
# 스택에다가 값을 push, ()->2 , []->3
#(2) 스택의 두번째 위에 여느 괄호가 있는 경우
# 스택에서 맨위에 있는 값과, 두번째 위에 있는 여는 괄호 모두 pop
# 스택에다가 값을 push,(X)->2X ,[X]->3X
#(3) 스택의 맨 위 둘다 값이라면, 합친다.
com=input()
result=[0]*50
myTop=0

for i in range(len(com)):
  if com[i]=="(" or com[i]=="[":
    if com[i]=="(":
      result[myTop]=-1
    else:
      result[myTop]=-2
    myTop+=1
  else:
    if result[myTop-1]==-1 or result[myTop-1]==-2:
      if com[i]==")" and result[myTop-1]==-1:
        myTop-=1
        result[myTop]=0
        result[myTop]=2
        myTop+=1
      elif com[i]=="]" and result[myTop-1]==-2:
        myTop-=1
        result[myTop]=0
        result[myTop]=3
        myTop+=1
      else:
        print("0")
        break
    else:
      myValue=result[myTop-1]
      myTop-=1
      result[myTop]=0
      if com[i]==")" and result[myTop-1]==-1:
        myTop-=1 
        result[myTop]=0
        result[myTop]=2*myValue 
        myTop+=1
      elif com[i]=="]" and result[myTop-1]==-2:
        myTop-=1 
        result[myTop]=0
        result[myTop]=3*myValue 
        myTop+=1
      else:
        print("0")
        break

    if result[myTop-1]>0 and result[myTop-2]>0:
      result[myTop-2]+=result[myTop-1]
      myTop-=1 
      result[myTop]=0

      
if myTop!=0:
  print("0")
else:
  print(result[0])
