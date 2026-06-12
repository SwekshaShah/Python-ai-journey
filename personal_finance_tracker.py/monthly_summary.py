transactions=[]
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