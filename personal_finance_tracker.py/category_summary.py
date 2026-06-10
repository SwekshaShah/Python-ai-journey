transactions=[]
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