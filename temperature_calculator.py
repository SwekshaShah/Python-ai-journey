temp= float(input("Enter temperature:"))
choice= input("Enter direction ie. f , k, c")
choice1= choice.upper()
temp1= temp*9/5+32 if choice1=="C INTO F" else temp*9/5+273.15 if choice1=="C INTO K" else (temp-32)*5/9 if choice1=="F INTO C" else temp
print(f"{temp}C is {temp1:.2f} in {choice}.")