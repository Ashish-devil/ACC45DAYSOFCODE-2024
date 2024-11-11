for i in range(int(input())):
    N,M= map(int,input().split())
    
    if M>=N:
        print(N)
    else:
        print(N-M+N)
