cart=[]
def show_cart():
    if not cart:   # or if cart==[]:
        print("Your cart is empty:")
        return
    print("Your cart")
    total=0
    for i, item in enumerate(cart):
        print(f"{i+1}.{item["name"]:<15}{item["price"]:>6.2f}")
        total+=item['price']
    print()
    print(f"{"total":<15} {total:>6.2f}")

def add_item():
  name= input("Enter item name:")
  name.strip()
  if not name:
    print("name cannort be empty:")
    return
  try:
    price=float(input("Enter price of item:"))
    if price<=0:
       print("only postive number:")
       return
  except ValueError:
    print("Invalid price")
  item={"name":name,"price":price}
  cart.append(item)
  print("Added to cart")

def remove_cart():
  if not cart:
    print("cart is empty-nothing to remove")
    return
  show_cart()

  n=int(input("Remove item name:"))
  if 1<=n<=len(cart):
    remove=cart.pop(n-1)
    print(f"Removed['name']")
  else:
     print("Invalid")

def search_cart(query):
   #query=input("search item name:")
   query=query.lower()
   results=[item for item in cart if query in item['name'].lower()]
   for item in cart:
    if query in item['name']:
        print("searched")
    else:
       print(f"No the {query} in not in cart")

def find_duplicates():
    names = [item['name'].lower() for item in cart]

    duplicates = set()

    for name in names:
        if names.count(name) > 1:
            duplicates.add(name)
    if duplicates:
        print("Duplicates:", ", ".join(duplicates))
    else:
        print("No duplicates.")
    