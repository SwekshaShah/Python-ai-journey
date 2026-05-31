for i in range(2,200):
  for j in range(2,i):
    if i%j==0:
      print(i)
      break
  else:
    print(f"Prime:{i}")