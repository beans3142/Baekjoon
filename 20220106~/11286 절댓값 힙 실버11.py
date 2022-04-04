class node:
    def __init__(self,key):
        self.value=key

    def key(self):
        return self.value

    def key(self,k):
        self.value=k

    def get_int(self):
        return int(self.value)

class heapq():
    mxsize=100001
    def __init__(self):
        self.heapsize=0
        self.array=[None for _ in range(heapq.mxsize)]

    def parent(self,cur):
        return cur//2

    def left(self,cur):
        return cur*2

    def right(self,cur):
        return cur*2+1

    def is_empty(self):
        if self.heapsize==0:
            return True
        return False

    def push(self,key):
        self.heapsize+=1
        self.array[self.heapsize]=key
        cur=self.heapsize
        par=self.parent(cur)

        while cur!=1:
            if self.array[par]<self.array[cur]:
                self.array[par],self.array[cur]=self.array[cur],self.array[par]
                cur=par
            else:
                break

    def bigger(self,cur):
        if cur*2>self.heapsize:
            return None
        elif cur*2==self.heapsize:
            return cur*2
        else:
            if self.array[cur*2]>self.array[cur*2+1]:
                return cur*2
            else:
                return cur*2+1

    def pop(self):
        if self.is_empty():
            return 0
        ret=self.array[1]
        temp=self.array[self.heapsize]
        cur_idx=1
        big=self.bigger(cur_idx)
        while big and temp<self.array[big]:
            self.array[cur_idx]=self.array[big]
            cur_idx=big
            big=self.bigger(cur_idx)
            self.array[cur_idx]=temp
        self.heapsize-=1
        return ret

from random import *

h=heapq()

r_arr=sample(list(range(randint(1,1000))),randint(7,15))

print(r_arr)

for i in r_arr:
    #h.push(node(i))
    h.push(i)
    
print(h.array[1:len(r_arr)+1])

for i in range(len(r_arr)):
    print(h.pop())
