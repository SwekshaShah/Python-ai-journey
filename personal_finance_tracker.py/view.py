transactions=[]
def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    
    total=0
    for i,t in enumerate(transactions):
        print(f"{i+1}.{t['desccription']:<20} {t['amount']:>8.2f}")
        total+=t['amount']
    print(f"Total: {total:.2f}")