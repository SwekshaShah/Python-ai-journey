restaurants=[]
def add():
  n= int(input("How many item do you want in menu:"))
  for i in range(n):
    item_name = input("Enter item name:")
    price = int(input("Enter price:"))
    category = input("Enter category:")
    restaurant = {
        'name': item_name,
        'price': price,
        'category': category
    }
    restaurants.append(restaurant)
    print("Added")
    print(f"Name:{item_name:<20} price:{price:<10}")
  print(restaurants)

def view_menu():
    if not restaurants:
        print("No menu entered yet.")
        return

    total=0
    for i,t in enumerate(restaurants):
        print(f"{i+1}.{t['name']:<20} {t['price']:>8.2f}")
        total+=t['price']
    print("="*32)
    print(f"Total: {total:.2f}")

def get_by_category(category):
  print(f"restaurant in category {category}:")
  for t in restaurants:
    if t['category'].lower()==category.lower():
      print(f"{t['name']:<20} {t['price']:>8.2f}")

def get_total_cost():
    total_cost=0
    for t in restaurants:
      total_cost+=t['price']
    return
get_total_cost()

def filter_menu(**menu):
  results=restaurants.copy()
  if 'category' in filter:
      results=[t for t in results if t['category']==menu['category'].lower()]
  if 'category' in filter:
    print(f"category:{menu['category'].title()}")

  print(f"{'SNo.':<8} {'name':<20} {'price':>10}") #header

  for i,t in enumerate(results,start=1):
      print(f"{i:<8} {t['name']:<20} {t['price']:>10.2f}")
  print("_"*47)

def menu():
  print("----------Restaurant Menu----------")
  while True:
    print("\n  1. Add  2. View  3. By_category  4. Balance 5.Filter_menu 6.Exist")
    choice=input("choose").strip()
    if choice=='1':
      add()
    elif choice=='2':
      view_menu()
    elif choice=='3':
      category=input("enter category")
      get_by_category(category)
    elif choice=='4':
      get_total_cost()
    elif choice=='5':
      filter1=input("enter category to filter")
      filter_menu(filter1=filter1)
    elif choice=='6':
      break
    else:
      print("invalid choice")
menu()
           
