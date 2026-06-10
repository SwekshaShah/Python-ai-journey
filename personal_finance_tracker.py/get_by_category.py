transactions=[]
def get_by_category(category):
  print(f"Transactions in category {category}:")
  for t in transactions:
    if t['category']==category:
      print(f"{t['description']:<20} {t['amount']:>8.2f}")