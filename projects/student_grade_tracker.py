students = {
    "Ram": {
        "English": 80,
        "Science": 90,
        "Math": 85
    },
    "Sita": {
        "English": 95,
        "Science": 88,
        "Math": 91
    },
    "Gita": {
        "English": 89,
        "Science": 94,
        "Math": 87
    },
    "Shyam": {
        "English": 68,
        "Science": 74,
        "Math": 71
    },
    "Rita": {
        "English": 92,
        "Science": 96,
        "Math": 94
    },
    "Anita": {
        "English": 81,
        "Science": 79,
        "Math": 84
    },
    "Bikash": {
        "English": 73,
        "Science": 77,
        "Math": 75
    },
    "Kiran": {
        "English": 98,
        "Science": 95,
        "Math": 99
    },
    "Sunita": {
        "English": 86,
        "Science": 84,
        "Math": 88
    }}

def add_students_grade():
    n = int(input("Enter how many students' grades do you want to store: "))

    for i in range(n):
        name = input("Name: ")
        english = int(input("English score: "))
        science = int(input("Science score: "))
        math = int(input("Math score: "))

        students[name] = {
            "English": english,
            "Science": science,
            "Math": math
        }

    print("\nStudent Records:")
    print(f'{"Name":<20}{"English":<20}{"Science":<20}{"Math":<20}')

    for name, marks in students.items():
        print(f"{name:<20}{marks['English']:<20}{marks['Science']:<20}{marks['Math']:<20}")

def view_student():
    if not students:
        print("No students yet.")
        return
    
    total=0
    for i,t in enumerate(students):
        print(f"{i+1}.{t['name']:<20} {t['price']:>8.2f}")
        total+=t['price']
    print(f"Total: {total:.2f}")
def get_average(Name):
  for name in students:
    if name == Name:
      english = students[name]['English']
      science = students[name]['Science']
      math = students[name]['Math']
      average = (english + science + math) / 3
      print(f"Average:{average}")
      return average
    
def top_student():
    top_list = []
    top_student_name=""
    top_score=0

    for name, mark in students.items():
        score = sum(mark.values())
        percentage=score/3
        top_list.append((name, score,percentage))
    print()
    top_list.sort(key=lambda x: x[1], reverse=True)
    print(f"{'Name':<20} {'Score':<20}")
    for i in top_list[:5]:
      print(f"{i[0]:<20} {i[1]:<20}")
    print("_"*27)
    top_student_name = top_list[0][0]
    top_score = top_list[0][1]
    print(f"Name:{top_student_name} Score:{top_score}")

def menu():
  print("----------Student Grade Tracker----------")
  while True:
    print("\n  1. Add  2. View   3. Average  4. Topper Student 5.Exit")
    choice=input("choose").strip()
    if choice=='1':
      add_students_grade()
    elif choice=='2':
      view_student()
    elif choice=='3':
      name=input("enter name")
      print("Average:",(get_average('name')))
    elif choice=='4':
      top_student()
    elif choice=='5':
      break
    else:
      print("invalid choice")
menu()
           
