
for i in range(int(input())):
    A,B,C=map(int,input().split())
    if A<=B and B>=C:
        print("Yes")
    else:
        print("No")
