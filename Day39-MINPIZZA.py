for i in range(int(input())):

    N,X = map(int,input().split())

    P = (N*X)//4
    if (N*X)%4 == 0:
        print(P)
    else:
        print(P+1)

