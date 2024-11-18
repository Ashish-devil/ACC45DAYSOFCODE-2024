for i in range(int(input())):

    N,X=map(int,input().split())

    X=X%N
    if(X==0):
        print("YES")
    else:
        print("NO")