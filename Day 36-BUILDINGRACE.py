for i in range(int(input())):

    A,B,X,Y=map(int,input().split())
    if(A/X<B/Y):
         print("Chef")
    elif(A/X>B/Y):
         print("Chefina")
    else:
         print("Both")
