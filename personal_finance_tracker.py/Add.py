transactions=[]
"""
def add_transaction(description, amount,category):
    transaction = {
        'description': description,
        'amount': amount,
        'category': category
    }
    transactions.append(transaction)
    print(f"Added:{description} {amount}")

def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    
    total=0
    for i,t in enumerate(transactions):
        print(f"{i+1}.{t['desccription']:<20} {t['amount']:>8.2f}")
        total+=t['amount']
    print(f"Total: {total:.2f}")

def get_balance():
    balance=0
    for t in transactions:
        balance+=t['amount']
        return balance
#return sum(t['amount] for t in transactions)
def get_by_category(category):
  print(f"Transactions in category {category}:")
  for t in transactions:
    if t['category']==category:
      print(f"{t['description']:<20} {t['amount']:>8.2f}")
get_by_category('food')

def category_summary():
  summary={}
  for t in transactions:
    category=t['category']
    if category in summary:
      summary[category]+=t['amount']
    else:
      summary[category]=t['amount']
  print("\n  --- Spending by Category ---")
  for i, total in sorted(summary.items()):
    print(f"  {i:<20} {total:>8.2f}")
category_summary()
"""

"""
def filter_transactions(**filter):
    results=transactions.copy()
    if 'category' in filter:
        results=[t for t in results if t['category']==filter['category']]
    print(filter['catergory'])
filter_transactions(category='food')
"""

transactions = [
    {'description': "momo", 'amount': 150, 'category': "food"},
    {'description': "coffee", 'amount': 300, 'category': "drink"},
    {'description': "kitkat", 'amount': 50, 'category': "chocolate"},
    {'description': "cake", 'amount': 100, 'category': "food"},
    {'description': "pizza", 'amount': 450, 'category': "food"},
    {'description': "burger", 'amount': 250, 'category': "food"},
    """{'description': "coke", 'amount': 80, 'category': "drink"},
    {'description': "tea", 'amount': 40, 'category': "drink"},
    {'description': "ice cream", 'amount': 120, 'category': "dessert"},
    {'description': "chips", 'amount': 60, 'category': "snack"},
    {'description': "donut", 'amount': 90, 'category': "dessert"},
    {'description': "sandwich", 'amount': 180, 'category': "food"},
    {'description': "juice", 'amount': 110, 'category': "drink"},
    {'description': "chocolate bar", 'amount': 70, 'category': "chocolate"},
    {'description': "fries", 'amount': 130, 'category': "snack"}"""
]
def get_balance():
    balance=0
    for t in transactions:
        balance+=t['amount']
        return balance
get_balance()

