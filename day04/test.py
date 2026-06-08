cart = [
    {"name": "bag", "price": 1000},
    {"name": "book", "price": 3000},
    {"name": "shoes", "price": 5000}
]

def search_cart():
    query = input("Search item name: ").lower()

    results = [item for item in cart if query in item['name'].lower()]

    if results:
        print("Search results:")
        for item in results:
            print(f"{item['name']:<15}{item['price']:<6.2f}")
    else:
        print(f"No '{query}' found in cart")

search_cart()