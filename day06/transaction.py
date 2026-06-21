import json
import os
from datetime import datetime


class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now().isoformat()

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        t = cls(
            data["description"],
            data["amount"],
            data["category"]
        )
        t.date = data.get("date", datetime.now().isoformat())
        return t

    def __str__(self):
        return f"{self.description}: Rs{self.amount:.2f} [{self.category}]"


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add(self, description, amount, category):
        t = Transaction(description, amount, category)
        self.transactions.append(t)
        return t

    def get_balance(self):
        return sum(t.amount for t in self.transactions)

    def get_category(self, category):
        return [
            t for t in self.transactions
            if t.category.lower() == category.lower()
        ]

    def filter(self, **filters):
        result = self.transactions.copy()

        if "category" in filters:
            cat = filters["category"].lower()
            result = [
                t for t in result
                if t.category.lower() == cat
            ]

        if "amount_min" in filters:
            result = [
                t for t in result
                if t.amount >= filters["amount_min"]
            ]

        return result

    def summary(self):
        print("\n--- Summary ---")
        print(f"Total Balance: Rs{self.get_balance():.2f}")
        print(f"Total Transactions: {len(self.transactions)}")

    def write_file(self, filename="transactions.json"):
        with open(filename, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f)

    def load(self, filename="transactions.json"):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as f:
            data = json.load(f)
            self.transactions = [Transaction.from_dict(d) for d in data]

        print(f"Loaded {len(self.transactions)} transactions.")


class User:
    user_count = 0

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now().isoformat()
        User.user_count += 1

    def greet(self):
        return f"I am {self.name}."


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Admin"

    def delete_all(self, tracker):
        count = len(tracker.transactions)
        tracker.transactions = []
        tracker.write_file()
        print(f"{self.name} deleted {count} transactions.")


def main():
    print("=== Personal Finance Tracker ===")

    user = User("Sweety")
    admin = Admin("Sara")

    print(user.greet())
    print(admin.greet())

    tracker = FinanceTracker()
    tracker.load()

    tracker.add("Groceries", 45.50, "food")
    tracker.add("Gas", 60.00, "transport")

    tracker.summary()

    tracker.write_file()

    print("Users:", User.user_count)


if __name__ == "__main__":
    main()