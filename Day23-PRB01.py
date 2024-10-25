for i in range(int(input())):

    a=int(input())

    N=0
    for i in range(1,a+1):
        if (a%i)==0:
            N=N+1
     
    if N==2:
        print("YES")
    else:
        print("NO")
