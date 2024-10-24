for i in range(int(input())):

        N=int(input())

        L=list(input().split())
        A=0
        B=0
        for i in L:
                if i=="START38":
                       A+=1
                else:
                        B+=1
        print(A,B)
