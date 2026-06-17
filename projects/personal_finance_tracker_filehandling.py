import json

transactions = [{'description': "momo", 'amount': 150, 'category': "food"},
    {'description': "coffee", 'amount': 300, 'category': "drink"},
    {'description': "kitkat", 'amount': 50, 'category': "chocolate"},
    {'description': "cake", 'amount': 100, 'category': "food"},
    {'description': "pizza", 'amount': 450, 'category': "food"},
    {'description': "burger", 'amount': 250, 'category': "food"}]
file_name = "transactions.json"


def save_transactions():
    with open(file_name, 'w') as file:
        json.dump(transactions, file, indent=4)


def load_transactions():
    global transactions
    try:
        with open(file_name, 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []


def add_transaction(description, amount, category):
    transaction = {
        'description': description,
        'amount': amount,
        'category': category.lower()
    }

    transactions.append(transaction)
    save_transactions()
    print(f"Added: {description} {amount}")


def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return

    total = 0

    print(f"\n{'SNo.':<8} {'Description':<20} {'Amount':>10}")

    for i, t in enumerate(transactions, start=1):
        print(f"{i:<8} {t['description']:<20} {t['amount']:>10.2f}")
        total += t['amount']

    print("-" * 40)
    print(f"Total: {total:.2f}")


def get_balance():
    balance = 0

    for t in transactions:
        balance += t['amount']

    return balance



def get_by_category(category):
    print(f"\nTransactions in category: {category}")

    found = False

    for t in transactions:
        if t['category'] == category.lower():
            print(f"{t['description']:<20} {t['amount']:>8.2f}")
            found = True

    if not found:
        print("No transactions found.")


def category_summary():
    summary = {}

    for t in transactions:
        category = t['category']

        if category in summary:
            summary[category] += t['amount']
        else:
            summary[category] = t['amount']

    print("\n--- Spending by Category ---")

    for category, total in sorted(summary.items()):
        print(f"{category:<20} {total:>8.2f}")


def filter_transactions(**filter):
    results = transactions.copy()

    if 'category' in filter:
        results = [
            t for t in results
            if t['category'] == filter['category'].lower()
        ]

    if 'amount_min' in filter:
        results = [
            t for t in results
            if t['amount'] > filter['amount_min']
        ]

    if 'amount_max' in filter:
        results = [
            t for t in results
            if t['amount'] < filter['amount_max']
        ]

    print(f"\n{'SNo.':<8} {'Description':<20} {'Amount':>10}")

    for i, t in enumerate(results, start=1):
        print(f"{i:<8} {t['description']:<20} {t['amount']:>10.2f}")

    print("_" * 47)


def get_monthly_summary():
    if not transactions:
        print("No transactions yet.")
        return

    total = get_balance()
    by_cat = {}

    for t in transactions:
        cat = t["category"]

        if cat not in by_cat:
            by_cat[cat] = 0

        by_cat[cat] += t["amount"]

    print("\n======== Monthly Summary ========")
    print("Total:", total)
    print("Transactions:", len(transactions))

    for cat, amount in by_cat.items():
        print(cat, ":", amount)

load_transactions()


def menu():
    print("---------- Personal Finance Tracker ----------")

    while True:
        print("\n1.Add  2.View all  3.Balance")
        print("4.By Category  5.Summary")
        print("6.Filter  7.Monthly  8.Exit")

        choice = input("Choose: ").strip()

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")

            add_transaction(description, amount, category)

        elif choice == '2':
            view_transactions()

        elif choice == '3':
            print("Balance:", get_balance())

        elif choice == '4':
            category = input("Enter category: ")
            get_by_category(category)

        elif choice == '5':
            category_summary()

        elif choice == '6':
            category = input(
                "Enter category you want to filter: "
            )

            filter_transactions(category=category)

        elif choice == '7':
            get_monthly_summary()

        elif choice == '8':
            print("Thank You")
            break

        else:
            print("Invalid choice")


menu()