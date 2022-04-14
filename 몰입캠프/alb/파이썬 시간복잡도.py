from time import *

arr=input()

arr.split()

for i in arr:
  if i.islower()==True:
    arr[arr.index(i)]=arr[arr.index(i)].upper()
  if i.isupper()==True:
    arr[arr.index(i)]=arr[arr.index(i)].lower()
    
print(arr)
