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
        print(f"{i+1}.{t['description']:<20} {t['amount']:>8.2f}")
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

def filter_transactions(**filter):
  results=transactions.copy()
  if 'category' in filter:
      results=[t for t in results if t['category']==filter['category'].lower()]
  if 'amount_min' in filter:
      results=[t for t in results if t['amount']>filter['amount_mini']]
  if 'amount_max' in filter:
      results=[t for t in results if t['amount']<filter['amount_max']]

  if 'category' in filter:
    print(f"category:{filter['category'].title()}")

  print(f"{'SNo.':<8} {'Description':<20} {'Amount':>10}") #header

  for i,t in enumerate(results,start=1):
      print(f"{i:<8} {t['description']:<20} {t['amount']:>10.2f}")
  print("_"*47)

def get_monthly_summary():
    if not transactions:
        return

    total = get_balance()
    by_cat = {}
    for t in transactions:
      cat = t["category"]
      if cat not in by_cat:
        by_cat[cat]=0
        by_cat[cat]+=t["amount"]
    print("\n======== Monthly Summary ========")
    print("Total:", total)
    print("Transactions:", len(transactions))
    for cat in by_cat:
      print(cat, ":", by_cat[cat])

def menu():
  print("----------Personal Finance Tracker----------")
  while True:
    print("\n  1. Add  2. View all  3. Balance  4. By_category 5.Summary 6.Filter 7.Monthly 8.Exit")
    choice=input("choose:").strip()
    if choice=='1':
      description=input("enter description:")
      amount=float(input("enter amount:"))
      category=input("enter category:")
      add_transaction(description,amount,category)
    elif choice=='2':
      view_transactions()
    elif choice=='3':
      print("balance:",get_balance())
    elif choice=='4':
      category=input("enter category:")
      get_by_category(category)
    elif choice=='5':
      category_summary()
    elif choice=='6':
      category=input("Enter the category you want to filter:")
      filter_transactions(category=category)
    elif choice=='7':
      get_monthly_summary()
    elif choice=='8':
      print("Thank You")
      break
    else:
      print("invalid choice")
menu()



