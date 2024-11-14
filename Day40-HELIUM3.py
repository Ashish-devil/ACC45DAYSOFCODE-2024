for i in range(int(input())):
    A=list(map(int,input().split()))
    if A[0]*A[1]<=A[2]*A[3]:
        print("Yes")
    else:
        print("No")