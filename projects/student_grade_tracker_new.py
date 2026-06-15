students=[
    {
        "name": "Ram",
        "math": 85,
        "english": 90,
        "science": 80
    },
    {
        "name": "Sita",
        "math": 95,
        "english": 92,
        "science": 88
    },
    {
        "name": "Hari",
        "math": 70,
        "english": 75,
        "science": 78
    },
    {
        "name": "Geeta",
        "math": 82,
        "english": 84,
        "science": 86
    }
]
def add_student(name, math, english, science):
    student = {
        "name": name,
        "math": math,
        "english": english,
        "science": science
    }
    students.append(student)

name=input("enter name:")
math=int(input("enter math:"))
english=int(input("enter english:"))
science=int(input("enter science:"))
add_student(name,math,english,science)

def view():
  for student in students:
    print(f"{student['name']:<20}{student['math']:<20}{student['english']:<20}{student['english']:<20}")

def average():
  print(f'{"Name":<10} {"Average Marks"}')
  for i in students:
    average=(i['math']+i['english']+i['science'])/len(students)
    print(f"{i['name']:<10} average: {average}")

def top5_student():
    top_list = []

    for data in students:
        score = data['math']+data['english']+data['science']
        percentage=score/3
        top_list.append((data['name'], score,percentage))
    top_list.sort(key=lambda x: x[1], reverse=True)
    print(f"{'SNo':<10}{'Name':<20} {'Score':<20}")
    
    for i, info in enumerate(top_list[:5]):
      print(f"{i:<10} {info[0]:<20} {info[1]:<20}")
    print("_"*35)
    topper=top_list[0]
    print(f"Top Student: {topper[0]} with score {topper[1]}")

def topper():
    top_list = top5_student() 
    topper = top_list[0]
    print(f"Top Name: {topper[0]} Score: {topper[1]}")

def menu():
  print("----------Student Grade Tracker----------")
  while True:
    print("\n  1. Add  2. View   3. Average  4. Topper Student 5.Exit")
    choice=input("choose").strip()
    if choice=='1':
      add_student()
    elif choice=='2':
      view()
    elif choice=='3':
      name=input("enter name")
      print("Average:",(average('name')))
    elif choice=='4':
      top5_student()
    elif choice=='5':
       topper()
    elif choice=='6':
      break