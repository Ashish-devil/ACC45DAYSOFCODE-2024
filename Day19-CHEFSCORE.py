for i in range(int(input())):

        N,X,Y=map(int,input().split())
        print("YES") if (Y%X==0) else print("NO")
