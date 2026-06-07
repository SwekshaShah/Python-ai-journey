import random
number= random.randint(1,100)
attempt=0
max_attempt=10
while attempt<max_attempt:
  guess= int(input("Enter a number:"))
  attempt+=1
  if guess==number:
    print("Correct answer! you won")
    print("Attempt",attempt)
    break
  elif guess>number:
    print("You are High")
  else:
    print("You are low")

if guess!=number:
  print("Game Over!")
  print("The number is:",number)

