choice_have= input("Enter direction in c or f or k:")
temp= float(input("Enter temperature in celcius:"))
choice_want= input("Enter direction in c or f or k:")
choice1= choice_have.upper()
choice2= choice_want.upper()
if choice1=="C" and choice2=="F":
  temp1=temp*9/5+32
elif choice1=="C" and choice2=="K":
  temp1=temp+273.15
elif choice1=="F" and choice2=="C":
  temp1= (temp-32)*5/9
elif choice1=="F" and choice2=="K":
  temp1= temp*9/5+273.15
elif choice1=="K" and choice2=="C":
  temp1= temp-273.15
elif choice1=="K" and choice2=="F":
  temp1= (temp-273.15)*9/5+32
else:
  print("Invalid Choice")

print(f"{temp:.2f}{choice_have} = {temp1:.2f}{choice_want}")