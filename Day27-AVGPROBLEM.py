for i in range(int(input())):

    A,B,C = map(int,input().split())

    if(((A+B)/2)>C):
        print("YES")
    else:
        print("NO")