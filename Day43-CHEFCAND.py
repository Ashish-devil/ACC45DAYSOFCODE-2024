from math import ceil
for i in range(int(input())):
    N,X = map(int, input().split())
    if X<N:
        print(ceil((N-X)/4))
    else:
        print(0)
