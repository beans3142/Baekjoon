from time import *

s=list('abcdabcdabcd'*15)
now=time()
for i in range(len(s)):
  print(s[i],end='')
print("")
print(time()-now)
now=time()
print(''.join(s))
print(time()-now)
