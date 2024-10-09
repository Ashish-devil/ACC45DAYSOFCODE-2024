for i in range(int(input())):
    N,X=map(int,input().split())
    if X!=N:
        print(min(X,N-X))
    else:
        print(0)

