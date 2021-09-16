from collections import defaultdict

def solution(gems):
    length=len(set(gems))
    vi=defaultdict(int)
    answer=(100001,0,0)
    start=end=0
    try:
        while:
            while len(vi)<length:
                vi[gems[end]]+=1
                end+=1
            while len(vi)==length:                
                vi[gems[start]]-=1
                if vi[gems[start]]==0:
                    del vi[gems[start]]
                    start+=1
                    break
                start+=1
            answer=min(answer,(end-start+1,start,end))
    except:
        return answer[1:]


tc=[]
tc.append(["diamond","diamond","diamond","ruby","diamond"])
tc.append(["xx",'yy','zz','xx','yy','cc'])
tc.append(["xx"])
tc.append(["xx","yy","xx","xx"])
tc.append(["xx","yy","xx","xx",'zz'])
tc.append(["xx","yy","xx","xx",'yy','yy','zz','xx'])

for i in tc:
    print(i)
    print(solution(i))
