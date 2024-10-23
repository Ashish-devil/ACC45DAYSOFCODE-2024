import math
for i in range(int(input())):

    H,X,Y=map(int,input().split())
    if X>=Y:
        print(math.ceil(H/X))
    else:
        print(math.ceil((H-Y)/X)+1)
