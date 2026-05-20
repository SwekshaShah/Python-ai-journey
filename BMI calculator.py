weight= float(input("Enter your weight:"))
height= float(input("Enter your height:"))
BMI=weight/(height**2)
if BMI<=18.5:
    print(f"{BMI:.1f}:Underweight")
elif 18.5<BMI<=24.9:
  print(f"{BMI:.1f}:normalweight")
elif BMI>=25:
  print(f"{BMI:.1f}:Overweight")