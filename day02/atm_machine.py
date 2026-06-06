balance=1000
deposit=int(input("Enter the amount you want to deposit:"))
withdraw=int(input("Enter the amount you want to withdraw:"))
print("Menu:1.Check balance 2.Deposite 3.Withdraw 4.Exit")
print("Do u want to check your balance before deposit of withdraw?")
print("If yes choice 1")
print("Do u want to know how much money you have deposit?")
print("If yes choice 2")
print("Do u want to know how much money you have withdraw?")
print("If yes choice 3")
print("Do u want the total balance after deposit and withdraw?:")
print("If yes choice 5:")
while True:
  choice=int(input("Enter your choice:"))
  if choice==1:
    print(f"Your balance {balance}")
  elif choice==2:
    if deposit<0:
      print("Can't deposite negative amount")
    else:
      print(f"your deposit {deposit}")
  elif choice==3:
    withdraw+=int(input("Enter the amount you want to withdraw . if u don't want to withdraw any amount please enter 0:"))
    print("The total amount you have with draw till now:")
    if withdraw>balance:
      print("Can't withdraw more than balance")
    else:
      print(f"you have withdraw {withdraw} amount")
  elif choice==4:
    print("Exit")
  elif choice==5:
    total_balance= balance+deposit+withdraw
    print(f"Your total balance after deposit and withdraw is {total_balance}")
  else:
    print("Invalid choice")