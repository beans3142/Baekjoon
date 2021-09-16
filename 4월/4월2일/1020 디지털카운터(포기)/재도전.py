from math import *
import sys

N=input()
iN=int(N)
numset={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5}
secondnum=0
time=0
firstnum=0
numof1=N.count('1')
i=1
siN=str(iN)

for i in range(0,len(N)):
    firstnum+=numset[N[i]]

if numof1==len(N):
    print(10**(len(N)))
    sys.exit()


if N[-3:]=='111':
    while N[-i]=='1':
        i+=1
    if int(N[-i])==9:
        time+=int('8'*(i-1))+1
        iN=0
    else:
        time+=10**(i-1)
        iN+=10**(i-1)

iN+=1
secondN='abc'

while firstnum!=secondnum:
    secondnum=0
    i=1
    if secondN[-3:]=='111':
        while secondN[-i]=='1':
            i+=1
        if secondN[-i]=='9':
            time+=int('8'*(i-1))+1
            iN+=int('8'*(i-1))+1
            if iN >= 10**len(N)-1:
                iN=0
                secondnum=6*len(N)
                iN+=1
                time+=1
        else:
            time+=10**(i-1)
            iN+=10**(i-1)
    elif iN >= 10**len(N)-1:
        iN=0
        secondnum=6*len(N)
        iN+=1
        time+=1
    else:
        secondN=''
    while len(N)!=len(secondN):
        if iN == 0:
            secondnum=str(6*len(N))
        else:
            secondN='0'*(len(N)-int(log10(iN))-1)+str(iN)
    for i in range(0,len(N)):
        secondnum+=numset[secondN[i]]
    iN+=1
    time+=1

print(time)
