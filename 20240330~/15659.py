from sys import stdin
input=stdin.readline

def bt(depth):
    global mx,mn
    if depth==n-1:
        v=eval(''.join(st))
        mx=max(v,mx)
        mn=min(v,mn)
        return
    for i in susik:
        if susik[i]!=0:
            st.append(i)
            susik[i]-=1
            st.append(str(arr[depth]))
            bt(depth+1)
            susik[i]+=1
            st.pop()
            st.pop()

n=int(input())

s,*arr=list(map(int,input().split()))
st=[str(s)]
usable=list(map(int,input().split()))
susik={'+':usable[0],'-':usable[1],'*':usable[2],'//':usable[3]}

mn=float('inf')
mx=-float('inf')
bt(0)

print(mx,mn,sep='\n')
