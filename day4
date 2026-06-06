cart=[]
def show_cart():
    if len(cart) == 0:
        print("Cart is empty")
        return

    total = 0

    for i,item in enumerate(cart):
      print(f"{i+1}.{item['name']:<15} {item['price']:>6.2f}")
      total = total + item["price"]
      print(f"{'Total':<15} {total:>6.2f}")

def add_item():
  name= input("Enter item name:")
  name.strip()
  if not name:
    return
  try:
    price=float(input("Enter price of item:"))
  except ValueError:
    print("Invalid price")
  if price<=0:
    return
  item={"name":name,"price":price}
  cart.append(item)
  print("Added to cart")

def remove_cart():
  if not cart:
    return
  show_cart()

  item1=int(input("Remove item name:"))
  n=item1.index()
  if 1<=n<=len(cart):
    remove=cart.remove(item1)
    print(f"Removed{item1}")

def search_cart(item_search):
    item_search= item_search.lower()
    results = [item for item in cart if item_search in item['name'].lower()]

    if results:
        print(f"Results for '{item_search}':")
        for item in results:
            print(f"{item['name']}:{item['price']:.2f}")
    else:
        print(f"No results for{item_search}.")



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

def sort_by_name(item):
    items=item['name'].lower()
    return items
def sort_by_price(item):
    items=item['price']
    return items
def sort_cart(by="name"):
    if by == "name":
        cart.sort(key=sort_by_name)
    elif by == "price":
        cart.sort(key=sort_by_price)

def cart_stats():
    if not cart: 
       return
    prices = [item['price'] for item in cart]
    print(f"Items:{len(prices)}")
    print(f"Total:{sum(prices):.2f}")
    print(f"Avg:{sum(prices)/len(prices):.2f}")
    print(f"Min:{min(prices):.2f}")
    print(f"Max:{max(prices):.2f}")
    
def main():
    print("menu:" \
    "1.show cart",
    "2.add items to cart",
    "3.remove items from cart",
    "4.search items from cart",
    "5.find duplicate items from cart",
    "6.sort cart",
    "7.cart status")
    while True:
        choice = input("  Choose (1-8): ").strip()
        if   choice=='1': show_cart()
        elif choice=='2': add_item()
        elif choice=='3': remove_cart()
        elif choice=='4': search_cart()
        elif choice=='5': find_duplicates()
        elif choice=='6': sort_cart()
        elif choice=='7': cart_stats()
        elif choice=='8': break
main()