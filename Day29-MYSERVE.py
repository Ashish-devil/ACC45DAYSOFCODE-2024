for i in range(int(input())):

    P,Q = map(int, input().split())

    T = P+Q
    if T % 4 == 1 or T % 4 ==0:
        print("Alice")
    else:
        print("Bob")
        
