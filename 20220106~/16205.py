typ,var=input().split()
varname=[]
if typ=='1':
    idx=0
    while idx<len(var):
        if var[idx].isupper():
            varname.append('_')
        varname.append(var[idx])
        idx+=1
elif typ=='3':
    varname.append(var[0])
    idx=1
    while idx<len(var):
        if var[idx].isupper():
            varname.append('_')
        varname.append(var[idx])
        idx+=1
else:
    varname=var
idx=1
print(varname[0].lower(),end='')
while idx<len(varname):
    if varname[idx]=='_':
        idx+=1
        print(varname[idx].upper(),end='')
    else:
        print(varname[idx],end='')
    idx+=1
print()
    
print(''.join(varname).lower())

idx=1
print(varname[0].upper(),end='')
while idx<len(varname):
    if varname[idx]=='_':
        idx+=1
        print(varname[idx].upper(),end='')
    else:
        print(varname[idx],end='')
    idx+=1
