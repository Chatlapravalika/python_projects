import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

# Add expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!\n")

# View expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

# Show total expense
def show_total():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"💰 Total Expense: ₹{total}\n")

# Show chart
def show_chart():
    categories = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    plt.bar(categories.keys(), categories.values())
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expense Tracker Chart")
    plt.show()

# Menu
while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Chart")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        show_chart()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!\n")