T=int(input())
for i in range(T):
    P,Q,R,S=map(int,input().split())
    if(P>(Q+R+S)):
        print("YES")
    elif(Q>(P+R+S)):
        print("YES")
    elif(R>(P+Q+S)):
        print("YES")
    elif(S>(P+Q+R)):
        print("YES")
    else:
        print("NO")
