for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=x*y
    s=(z/a)*100
    if s>50:
        print("yes")
    else:
        print("No")