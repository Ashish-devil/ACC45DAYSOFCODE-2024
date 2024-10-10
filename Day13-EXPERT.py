for i in range(int(input())):
    X,Y=map(int,input().split())
    if Y/X*100>=50:
        print("YES")
    else:
        print("NO")
