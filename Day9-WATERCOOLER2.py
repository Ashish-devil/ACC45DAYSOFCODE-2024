for i in range(int(input())):
    X,Y=map(int,input().split())
    if X>=Y:
        print("0")
    elif X<Y and Y%X!=0:
        print(Y//X)
    else:
        print((Y//X)-1)
        