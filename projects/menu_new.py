restaurants = {}
def add_item(category, item, price):
    if category not in restaurants:
        restaurants[category] = {}
    restaurants[category][item] = price
    
def view():
    print(f'{"SNo.":<10} {"Category":<20} {"Item":<20} {"Price":<20}')
    for category, items in restaurants.items():
        for i, (item, price) in enumerate(items.items()):
            print(f'{i+1:<10}{category:<20} {item:<20} {price:<20}')
    
def update_item():
    item_name=input("enter the item name you want to update:").capitalize()
    for category , item in restaurants.items():
        if item_name in item:
            new_price=int(input("Enter new price:"))
            restaurants[category][item_name]=new_price
    print("Successfully Updated")
    return

def delete_item():
    item_name=input("enter the item name you want to delete:").capitalize()
    for category , item in restaurants.items():
        if item_name in item:
            del restaurants[category][item_name]
    print("Deleted Successfully")
    return



menu = {
    "Food": {
        # Nepali / Local
        "Momo": 150,
        "Buff Momo": 160,
        "Chicken Momo": 180,
        "Veg Momo": 140,
        "Chowmein": 180,
        "Thukpa": 220,
        "Dal Bhat": 300,
        "Sel Roti Set": 200,

        # Fast Food
        "Pizza": 500,
        "Burger": 250,
        "Cheese Burger": 300,
        "Chicken Burger": 320,
        "Hot Dog": 200,
        "Sandwich": 150,
        "Club Sandwich": 280,

        # Rice Items
        "Fried Rice": 200,
        "Veg Fried Rice": 180,
        "Chicken Fried Rice": 250,
        "Egg Fried Rice": 220,
        "Biryani": 350,
        "Chicken Biryani": 400,
        "Veg Biryani": 300,

        # Curry Items
        "Chicken Curry": 400,
        "Mutton Curry": 600,
        "Paneer Curry": 300,
        "Fish Curry": 450,
        "Dal Curry": 180,

        # Snacks
        "Samosa": 50,
        "Pakora": 100,
        "Spring Roll": 120,
        "French Fries": 150,
        "Wings": 350,

        # Continental
        "Pasta": 350,
        "White Sauce Pasta": 380,
        "Red Sauce Pasta": 350,
        "Lasagna": 500,
        "Steak": 900,
        "Grilled Chicken": 450
    },

    "Drinks": {
        "Tea": 50,
        "Milk Tea": 60,
        "Black Tea": 50,
        "Coffee": 200,
        "Black Coffee": 180,

        "Coke": 80,
        "Pepsi": 80,
        "Fanta": 80,
        "Sprite": 80,

        "Juice": 120,
        "Mango Juice": 150,
        "Orange Juice": 150,
        "Apple Juice": 180,

        "Milkshake": 250,
        "Chocolate Shake": 300,
        "Strawberry Shake": 280,

        "Lassi": 180,
        "Salted Lassi": 170,

        "Water": 30,
        "Soda": 60,
        "Energy Drink": 150
    },

    "Desserts": {
        "Ice Cream": 150,
        "Chocolate Ice Cream": 180,
        "Vanilla Ice Cream": 150,
        "Brownie": 250,
        "Cake Slice": 200,
        "Cheesecake": 350,
        "Donut": 120,
        "Waffle": 300,
        "Pudding": 180
    },

    "Combo": {
        "Momo + Coke": 200,
        "Burger Combo": 350,
        "Pizza Combo": 550,
        "Thali Set": 400,
        "Fried Rice Combo": 300
    }
}

cart={}
total_bill=0
def view_menu():
    print("\n----- RESTAURANT MENU -----")

    for category, items in menu.items():
        print(f"{category}:")
        for item, price in items.items():
            print(f"{item} - Rs.{price}")   

def order_food():
    global total_bill
    while True:
        found=True
        item_name=input("Item name:").capitalize()
        for category,item in menu.items():
            if item_name in item:
                quantity=int(input("Quantity:"))
        
                if item_name in cart:
                    cart[item_name]+=quantity
                else:
                    cart[item_name]=quantity
        
                total_bill+=item[item_name]*quantity
                print("Item added to cart")
                break
    
    if not found:
        print("Item not found")
    choice=input("Do you want to order more items? (yes/no):").lower()
    
    if choice=="no":
        break
    
def bill():
    carts1=order_food()
    for item, qty in cart.items():
        for category, items in menu.items():
            if item in items:
                print(f"{item} x {qty} = Rs.{items[item] * qty}")
    print(f"Total Bill: Rs.{total_bill}")

def main():
    while True:
        print("\n===== RESTAURANT SYSTEM =====")
        print("1. Owner")
        print("2. Customer")
        print("3. Exit")

        user = input("Choose: ")

        # ---------------- OWNER ----------------
        if user == "1":
            while True:
                print("\n--- OWNER MENU ---")
                print("1. Add Item")
                print("2. View Menu")
                print("3. Update Item")
                print("4. Delete Item")
                print("5. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    add_item()
                elif choice == "2":
                    view_menu()
                elif choice == "3":
                    update_item()
                elif choice == "4":
                    delete_item()
                elif choice == "5":
                    break
                else:
                    print("Invalid choice")

        # ---------------- CUSTOMER ----------------
        elif user == "2":
            while True:
                print("\n--- CUSTOMER MENU ---")
                print("1. View Menu")
                print("2. Order Food")
                print("3. View Bill")
                print("4. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    view_menu()
                elif choice == "2":
                    order_food()
                elif choice == "3":
                    bill()
                elif choice == "4":
                    break
                else:
                    print("Invalid choice")

        elif user == "3":
            print("Thank you!")
            break

        else:
            print("Invalid input")


main()