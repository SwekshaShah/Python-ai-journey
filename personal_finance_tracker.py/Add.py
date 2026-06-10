transactions=[]
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




