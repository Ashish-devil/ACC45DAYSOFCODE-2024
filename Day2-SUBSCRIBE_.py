import math
for t in range(int(input())):
    n,x = map(int,input().split())
    print((math.ceil(n/6))*x)

