def getV(s1,s2):
    def check(idx):
        for i in range(idx,idx+len(s1)):
            if (s1[i-idx]==s2[i]=='2'):
                return False
        return True

    le=len(s2)
    s2=s2+'1'*len(s1)
    for i in range(le):
        if check(i):
            return max(i+len(s1),le)
    return 1e10

s1=input()
s2=input()
ans=len(s1)+len(s2)
print(min(ans,getV(s1,s2),getV(s2,s1)))
