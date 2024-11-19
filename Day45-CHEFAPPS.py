for i in range(int(input())):

        S,X,Y,Z=map(int,input().split())

        if (X+Y)+Z<=S:
                print("0")
        elif (X+Z)<=S or (Y+Z)<=S:
                print("1")
        else:
                print("2")
