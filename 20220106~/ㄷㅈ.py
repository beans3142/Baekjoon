N=input()

numset={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5}

numzero=len(N)-len(str(int(N)))
numsum=0

for i in range(0,len(str(int(N)))):
    numsum+=numset[N[-1-i]]

tgnum=numzero*6+numsum


