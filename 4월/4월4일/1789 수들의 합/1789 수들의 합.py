s=int(input())

minN=0
num=0

while minN<s:
    num+=1
    minN+=num
    
if minN==s:
    print(num)
else:
    print(num-1)
