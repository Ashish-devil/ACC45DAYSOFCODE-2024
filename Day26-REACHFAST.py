import math

for i in range(int(input())):

    A,B,K=map(int,input().split())
    print(math.ceil(abs(A-B)/K))
