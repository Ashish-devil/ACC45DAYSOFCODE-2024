for i in range(int(input())):

    C = 0

    N= int(input())
    S= input()
    for i in range(N - 1):
        if S[i] == S[i+1]:
            C+=1
    print(C)
