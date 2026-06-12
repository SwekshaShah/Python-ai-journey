def menu():
  print("----------Personal Finance Tracker----------")
  while True:
    print("\n  1. Add  2. View all  3. Balance  4. By_category 5.Summary 6.Filter 7.Monthly 8.Exist")
    choice=input("choose").strip()
    if choice=='1':
      description=input("enter description")
      amount=float(input("enter amount"))
      category=input("enter category")
      add_transaction(description,amount,category)
    elif choice=='2':
      view_transaction()
    elif choice=='3':
      print("balance:",get_balance())
    elif choice=='4':
      category=input("enter category")
      get_by_category(category)
    elif choice=='5':
      category_summary()
    elif choice=='6':
      filter_transactions()
    elif choice=='7':
      get_monthly_summary()
    elif choice=='8':
      break
    else:
      print("invalid choice")
menu()
           
