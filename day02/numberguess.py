import random
number= random.randint(1,100)
attempt=0
max_attempt=7
while attempt<max_attempt:
  guess= int(input("Enter a number:"))
  attempt+=1
  if guess!= number and attempt>max_attempt:
    print("Game Over!")
    print("The number is:",number)
  elif guess==number:
    print("Correct answer! you won congratulation")
    print(f"Attempt : {attempt}")
    break
  elif guess>number:
    print(f"incorrect you have {max_attempt-attempt} left")
    print("You are too High")
  else:
    print(f"incorrect you have {max_attempt-attempt} left")
    print("You are too low")

#if guess!=number:
 #   print("Game Over!")
  #  print("The number is:",number)