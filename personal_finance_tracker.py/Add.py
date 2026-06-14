transactions=[]
def add_transaction(description, amount,category):
    transaction = {
        'description': description,
        'amount': amount,
        'category': category
    }
    transactions.append(transaction)
    print(f"Added:{description} {amount}")

