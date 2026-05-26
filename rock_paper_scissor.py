import random
print("Choices: rock, paper, scissor")
choice= ["rock","paper","scissor"]
n=int(input("Enter the number of time you want to play:"))
user_score=0
computer_score=0
attempt=0
while attempt<n:
  user= input("Enter your choice or quit:")
  user1=user.lower()
  computer_choice= random.choice(choice)
  if user1=="quit":
    print("Thank You please come back")
    break
  elif user==choice:
    print("It is tie")
  elif (user=="rock" and computer_choice=="scissor"):
    user_score+=1
    print("You won")
  elif (user=="paper" and computer_choice=="rock"):
    user_score+=1
    print("You won")
  elif(user=="scissor" and computer_choice=="paper"):
    user_score+=1
    print("You won")
  elif user not in choice:
    print("Invalid choice! Try again.")
    continue
  else:
    computer_score+=1
    print("")
    print("Sorry i won! try again")
  attempt+=1
  if attempt==n:
    break
print("Game Over")
print("Your Score is:",user_score)
print("Computer Score is:",computer_score)
print("Thank You for playing")