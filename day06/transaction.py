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
  tracker=FinanceTracker()
  tracker.load()
  name=input("enter your name:")
  user=User(name)

  while True:
    print("------Finance Tracker-------:")
    print("1. Add Transaction")
    print("2. View all transactions")
    print("3. View balance")
    print("4. View transactions by category")
    print("5. Show summary")
    print("6. Save transactions")
    print("7. Exit")

    choice=int(input("Enter your choice(1 to 7):"))
    if choice==1:
      description=input("Enter description:")
      amount=float(input("Enter amount:"))
      category=input("Enter category:")
      tracker.add(description,amount,category)
      print("Transaction added")
    elif choice==2:
      if not tracker.transactions:
        print("No transactions found")
      else:
        for t in tracker.transactions:
          print(t)
    elif choice==3:
      balance=tracker.get_balance()
      print(f"Total Balance: Rs{balance:.2f}")
    elif choice==4:
      category=input("Enter category:")
      transactions=tracker.get_category(category)
      if not transactions:
        print("No transactions found")
      else:
        for t in transactions:
          print(t)
    elif choice==5:
      tracker.summary()
    elif choice==6:
      tracker.write_file()
      print("Transactions saved")
    elif choice==7:
      print("Thank You")
      break
    else:
      print("Invalid choice")

if __name__=="__main__":
  main()  



