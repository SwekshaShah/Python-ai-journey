transactions = []
def add_multiple(*data):
  for desc, amount, cat in data:
    transactions.append((desc,amount,cat))
    add_transaction(desc, amount, cat)
  print(transactions)