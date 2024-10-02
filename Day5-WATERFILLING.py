for i in range(int(input())):
    B1,B2,B3=map(int,input().split())
    T=[B1,B2,B3].count(0)
    if T>=2:
        print("Water filling time")
    else:
        print("Not now")
