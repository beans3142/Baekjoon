from random import *

반복횟수=randint(3,15)

print(반복횟수)

for i in range(반복횟수):
    sample([i for i in range(1,7)],6)
    print(*sample([i for i in range(1,7)],6))
