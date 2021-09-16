import math as m

N=input()

numset={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5}
print(tgnum)
numsum=0
line=0
time=0

for i in range(0,len(str(int(N)))):
    numsum+=numset[N[-1-i]]

if str(N)!=str(int(N)):
    numsum+=6*(len(N)-len(str(int(N))))

while numsum!=line:
    numzero=(len(N)-len(str(int(N))))
    if int(N)>10**len(N)-1:
        N='0'*len(N)
        time+=1
    elif numzero != 0:
        line+=6*numzero
        for i in range(0,len(str(int(N)))):
            line+=numset[N[-1-i]]
        time+=1
    print(time)
