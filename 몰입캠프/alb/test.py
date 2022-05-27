n,m=map(int,input().split())
arr=[0]*n # ⓐ 어차피 n자리는 고정이므로 *n
visited=[False]*10 # ⓑ 0~9 사용 체크

# ⓒ 항상 n<=m 이여야 출력이 정상적으로 작동합니다.
#    그 이유는 사용할 수 있는 숫자 m개보다 n이 큰 경우 cur이 n까지 도달하지 못합니다. 
#    m은 0~10 사이의 수이여야 합니다.

def recur(cur): # 중복 없이 출력
  if cur==n:
    print(*arr,sep='') # ⓔ 파이썬에서 한자리씩 출력하는 것은 매우 안좋습니다.
                       #    해당 부분을 고쳐준 것으로 40% 가량 빨라졌습니다.
    return
  for i in range(m):
    if visited[i]:
      continue

    arr[cur]=i
    visited[i]=True
    recur(cur+1)
    visited[i]=False

recur(0)

# 밑의 함수는 위의 함수와 달리 중복이 가능하도록 출력하는 것 입니다!


def recur(cur): # 중복 가능하게 출력 n은 상관 없고 m만 0~10 사이면 가능.
  if cur==n:
    print(*arr,sep='') 
    return

  for i in range(m):
    arr[cur]=i
    recur(cur+1)

