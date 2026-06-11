transactions=[]
def filter_transactions(**filter):
  results=transactions.copy()
  if 'category' in filter:
      results=[t for t in results if t['category']==filter['category'].lower()]
  if 'amount_mini' in filter:
      results=[t for t in results if t['amount']>filter['amount_mini']]
  if 'amount_max' in filter:
      results=[t for t in results if t['amount']<filter['amount_max']]
  
  if 'category' in filter:
    print(f"category:{filter['category'].title()}")

  print(f"{'SNo.':<8} {'Description':<20} {'Amount':>10}") #header
  
  for i,t in enumerate(results,start=1):
      print(f"{i:<8} {t['description']:<20} {t['amount']:>10.2f}")
  print("_"*47)