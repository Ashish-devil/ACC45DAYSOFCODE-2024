for i in range(int(input())):
    N,A,B=map(int,input().split())
    C=0
    while N>1:
        C+=1 
        N=N/2
        
    print((C*A)+((C-1)*B))
