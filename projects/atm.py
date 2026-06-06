pin= input("Enter 4 digit number:")
length_of_pin= len(pin)
print("Amount you have=200000")
deposit= int(input("Enter how much money you want to deposite:"))
withdraw= int(input("Enter how much money you want to withdraw:"))
pin1=int(input("enter 4 digit pin that you have saved:" ))

if length_of_pin<4:
  print("Enter 4 digit pin only")
elif length_of_pin>4:
  print("Enter 4 digit pin only")
elif length_of_pin==4 and pin1==pin:
  print("correct")
print("choice:1.Check Balance,2.Deposit Money,3.Withdraw Money,4.Total amount after deposit,5.Total amout after withdraw,6.Exit")
choice={1:"Check Balance",2:"Deposit Money",3:"Withdraw Money",4:"Total_amount_after_deposit",5:"Total_amount_after_withdraw",6:"Exit"}

while True:
  enter_choice=int(input("Enter choice:"))
  if enter_choice==1:
    print(f"Your balance is:{amount}")
  elif enter_choice==2:
    print(f"Your deposited amount is:{deposit}")
  elif enter_choice==3:
    print(f"Your withdraw amount is:{withdraw}")
  elif enter_choice==4:
    print(f"Your total balance after depositing the money is:{amount+deposit}")
  elif enter_choice==5:
    print(f"Your total balance after depositing the money is:{amount-withdraw}")
  elif enter_choice==6:
    print("Exit")
    break
  else:
    print("Enter correct choice")
    break
