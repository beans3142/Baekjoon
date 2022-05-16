from sys import stdin
from collections import defaultdict
input=stdin.readline

def ptall():
    print('기호','이름','총 의석','받은 표','지역구','득표율','비례득','1단계','2단계','3단계',sep='\t\t\t')
    for i in res:
        print(no[i],i[:5],*res[i],sep='\t\t\t')
        

def stage1(pi,ri):
    result=((300-R)*pi-ri)/2
    if result<1:
        return 0
    return round(result)

def stage2(si,pi):
    return si+(leftasi)*pi
    

p,v=map(int,input().split())
res=defaultdict(list)
totalvoted=0
nowleftlocal=253
N=300
R=0
no={}

for i in range(p):
    name,localcnt,getvote=input().rstrip().split()
    no[name]=i
    localcnt=int(localcnt)
    getvote=int(getvote)
    res[name].extend([localcnt,getvote,localcnt])
    totalvoted+=getvote
    nowleftlocal-=localcnt

# R 값 계산
R=nowleftlocal


# 투표율 추가 및 의석할당정당 체크
propable=[]
propvoted=0

for i in res:
    votedper=res[i][1]/totalvoted
    res[i].append(votedper)
    if votedper>=0.03 or res[i][0]>=5:
        propable.append(i)
        propvoted+=res[i][1]
    else:
        R+=res[i][0]
        res[i].extend([0,0,0,0])

for i in propable:
    res[i].append(res[i][1]/propvoted)

s_asi=0
cangetprop=[]

for dang in propable:
    asi=stage1(res[dang][4],res[dang][0])
    res[dang].append(asi)
    if asi>0:
        cangetprop.append(dang)
    else:
        res[dang].extend([0])
    s_asi+=asi

if s_asi>30:
    leftasi=30
    sosujum=[]
    for i in cangetprop:
        val=30*res[i][5]/s_asi
        res[i].append(int(val))
        leftasi-=int(val)
        sosujum.append([-(val-int(val)),no[i],i])
    if leftasi>0:
        sosujum.sort()
        for i in range(leftasi):
            res[sosujum[i][2]][6]+=1
elif s_asi<30:
    leftasi=30
    sosujum=[]
    for i in cangetprop:
        val=res[i][5]+(30-s_asi)*res[i][4]
        res[i].append(int(val))
        leftasi-=int(val)
        sosujum.append([-(val-int(val)),no[i],i])
    if leftasi>0:
        sosujum.sort()
        for i in range(leftasi):
            res[sosujum[i][2]][6]+=1
else:
    for i in res:
        res[i].append(res[5])

# 3단계
leftasi=17
sosujum=[]
for i in propable:
    val=17*res[i][4]
    res[i].append(int(val))
    leftasi-=int(val)
    sosujum.append([-(val-int(val)),no[i],i])

sosujum.sort()
for i in range(leftasi):
    res[sosujum[i][2]][7]+=1

last=[]
for i in res:
    res[i][0]+=res[i][6]+res[i][7]
    last.append([-res[i][0],i])

last.sort()
for euwonsu,dangname in last:
    print(dangname,-euwonsu)
    
#ptall()

'''
in

5 1000
a 150 400
b 100 300
c 2 100
d 1 100
e 0 100

out
a 157
b 105
c 14
d 13
e 11

in
5 1000
a 50 200
b 50 200
c 50 200
d 50 200
e 50 200

out
a 60
b 60
c 59
d 59
e 59

in
5 1000
a 250 995
b 1 2
c 1 1
d 1 1
e 0 1

out
a 297
b 1
c 1
d 1
e 0

in
8 722715
A 156 364739
B 12 31633
C 66 321147
D 19 1720
E 0 86
F 0 805
G 0 844
H 0 1686

out
A 165
C 103
D 19
B 13
E 0
F 0
G 0
H 0
'''
