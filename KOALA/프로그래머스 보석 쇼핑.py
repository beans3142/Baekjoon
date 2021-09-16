# 보자마자 든 생각은 투 포인터 문제이다.
# 같은 보석이 나왔을 때 이전의 블럭을 "PASS"와 같이 바꿔준다? <- 번거로울듯
# 차라리 길이가 1인 배열이 아니라면 투 포인터의 왼쪽 값+1의 값과 왼쪽 값이 같다면
# 넘기는 형식이 더좋을 듯?

# 일단 set로 변경 ( 이걸 안할 방법은 없을까?)
# set안에 들어있는 원소들에 대해 0~그 길이까지 인덱스를 갖는 딕셔너리를 만들어줌
# ex ( dia:0 ruby:1 shapphire:2 ...}
# 그리고 그 길이만큼 등장 횟수를 저장해줄 set의 길이와 같은 리스트를 생성해줌
# [0,0,0,0...]
# 파이썬의 특징을 활용한 큰 수 연산, 비트로 표시해주고 최대 2**100000이긴 한데..
# 일단 잘 돌아가는거 같으니까 써보자.. => 아마 메모리? 사용량은 최악..

gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems=["AA", "AB", "AC", "AA", "AC"]
#gems=["XYZ", "XYZ", "XYZ"]
#gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

def sol(gems):
    gemlist={gem:idx+1 for idx,gem in enumerate(set(gems))}
    gem_cnt=[0]*(len(gemlist)+1)
    all_gem_value=len(gemlist)*(len(gemlist)+1)/2 # 모든 젬이 합쳐진 값(n(n+1)/2)
    nowvalue=0
    start=0
    end=0
    ans=[100001,0,0]
    while True:
        try:
            while nowvalue!=all_gem_value:
                if gem_cnt[gemlist[gems[end]]]==0:
                    nowvalue+=gemlist[gems[end]]
                gem_cnt[gemlist[gems[end]]]+=1
                end+=1
            while start<end:
                gem_cnt[gemlist[gems[start]]]-=1
                if gem_cnt[gemlist[gems[start]]]==0:
                    nowvalue-=gemlist[gems[start]]
                    end-=1
                    break
                start+=1
            dis=end-start+1
            if ans[0]>dis:
                ans=[dis,start,end]
                if dis==len(gemlist):
                    break

        except:
            break
    return [ans[1]+1,ans[2]+1]
            
a=sol(gems)

