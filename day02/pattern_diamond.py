n=int(input("enter a number:"))
for i in range(1,n+1):
  sp=" " * (n-i)
  print(sp + "* "*i)
for i in range(n,0,-1):
  sp=" " * (n-i)
  print(sp+"* "*i)