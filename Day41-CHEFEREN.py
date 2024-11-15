for i in range(int(input())):

    N,A,B = map(int,input().split())

    print(B*(N%2)+(A+B)*(N//2))
