
for i in range(int(input())):
  A,B,C,D,E,F=map(int,input().split())
  Alice=(A+B+C)-min(A,B,C)
  Bob=(D+E+F)-min(D,E,F)
  if Alice>Bob:print("Alice")
  elif Bob>Alice:print("Bob")
  else:print("Tie")
