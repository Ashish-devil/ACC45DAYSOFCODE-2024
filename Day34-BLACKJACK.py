for i in range(int(input())):

    A,B=map(int,input().split())

    if(A+B>=11):
        print(21-(A+B))
    else:
        print(-1)
