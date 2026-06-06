weight= float(input("Enter your weight:"))
height= float(input("Enter your height:"))
BMI=weight/(height**2)
if BMI< 18.5:
    print("Underweight")
elif 18.5<BMI<24.9:
    print("normalweight")
elif 25<BMI<29.9:
    print("Class 1 Obesity")
elif 30<BMI<39.9:
    print("Class 2 Obesity")
else:
    print("Class 3 Obesity")