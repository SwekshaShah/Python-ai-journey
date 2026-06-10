transactions=[]
def get_balance():
    balance=0
    for t in transactions:
        balance+=t['amount']
        return balance