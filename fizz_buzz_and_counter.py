fizz=0
buzz=0
fizzBuzz=0
bazz=0
fizzBazz=0
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
    fizzBuzz+=1
  elif i%3==0 and i%7==0:
    print("FizzBazz")
    fizzBazz+=1
  elif i%3==0:
    print("Fizz")
    fizz+=1
  elif i%5==0:
    print("Buzz")
    buzz+=1
  elif i%7==0:
    print("Bazz")
    bazz+=1
  else:
    print(i)

print(f"fizz has repeated for {fizz}")
print(f"Buzz has repeated for {buzz}")
print(f"FizzBuzz has repeated for {fizzBuzz}")
print(f"Bazz has repeated for {bazz}")
print(f"FizzBazz has repeated for {fizzBazz}")