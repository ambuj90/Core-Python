# 🛒 Dictionary of items with prices
# items = {
#     "Laptop": 800,
#     "Mouse": 25,
#     "Keyboard": 50,
#     "Monitor": 150,
#     "Headphones": 120,
#     "Pen": 5,
#     "Chair": 200,
#     "Notebook": 15
# }

# # 🔍 Filter items costing more than $100
# filtered_items = {item: price for item, price in items.items() if price > 100}

# # 📊 Display results
# print("🟢 Items costing more than $100:")
# for item, price in filtered_items.items():
#     print(f"{item}: ${price}")
    
    
    
# # 🛒 Step 1: Dictionary of items with prices
# items = {
#     "Laptop": 800,
#     "Mouse": 25,
#     "Keyboard": 50,
#     "Monitor": 150,
#     "Headphones": 120,
#     "Pen": 5,
#     "Chair": 200,
#     "Notebook": 15
# }

# # 🔍 Step 2: Create an empty dictionary to store filtered items
# filtered_items = {}

# # 🔄 Step 3: Filter items costing more than $100
# for item, price in items.items():  # Loop through each item and its price
#     if price > 100:                # Check if the price is greater than 100
#         filtered_items[item] = price  # Add the item to the new dictionary

# # 📊 Step 4: Display the filtered results
# print("🟢 Items costing more than $100:")
# for item, price in filtered_items.items():
#     print(f"{item}: ${price}")



# # 🛒 Step 1: Dictionary of items with prices
# items = {
#     "Laptop": 800,
#     "Mouse": 25,
#     "Keyboard": 50,
#     "Monitor": 150,
#     "Headphones": 120,
#     "Pen": 5,
#     "Chair": 200,
#     "Notebook": 15
# }

# # 🔄 Step 2: Display all items with prices
# print("\n📦 All Available Items:")
# for item, price in items.items():
#     print(f"{item}: ${price}")

# # 🔍 Step 3: Get user input for price filter
# try:
#     user_price = float(input("\n💰 Enter the minimum price to filter items: "))
# except ValueError:
#     print("❌ Invalid input! Please enter a number.")
#     exit()

# # 🟢 Step 4: Filter items based on user input
# filtered_items = {item: price for item, price in items.items() if price > user_price}

# # ❓ Step 5: Ask user if they want to sort the results
# sort_order = input("\n📊 Do you want to sort results by price? (yes/no): ").lower()

# if sort_order == "yes":
#     order = input("🔼 Type 'asc' for ascending or 'desc' for descending: ").lower()
#     if order == "asc":
#         filtered_items = dict(sorted(filtered_items.items(), key=lambda x: x[1]))
#     elif order == "desc":
#         filtered_items = dict(sorted(filtered_items.items(), key=lambda x: x[1], reverse=True))
#     else:
#         print("⚠️ Invalid sorting option. Showing unsorted results.")

# # 📊 Step 6: Display the filtered and sorted results
# print("\n🟢 Items costing more than ${:.2f}:".format(user_price))
# if filtered_items:
#     for item, price in filtered_items.items():
#         print(f"{item}: ${price}")
# else:
#     print("❌ No items found above this price.")


import csv

# 🛒 Step 1: Dictionary of items with prices
items = {
    "Laptop": 800,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 150,
    "Headphones": 120,
    "Pen": 5,
    "Chair": 200,
    "Notebook": 15
}

# 🟢 Function to display all items
def display_items():
    print("\n📦 All Available Items:")
    for item, price in items.items():
        print(f"{item}: ${price}")

# 🟡 Function to add new items
def add_new_item():
    while True:
        new_item = input("\n➕ Enter new item name (or type 'done' to finish): ").capitalize()
        if new_item.lower() == 'done':
            break
        try:
            new_price = float(input(f"💰 Enter price for {new_item}: $"))
            items[new_item] = new_price
            print(f"✅ {new_item} added successfully!")
        except ValueError:
            print("❌ Invalid price. Please enter a valid number.")

# 🔍 Function to filter items by user-defined price
def filter_items(min_price):
    return {item: price for item, price in items.items() if price > min_price}

# 🔼 Function to sort items by price
def sort_items(filtered, order):
    return dict(sorted(filtered.items(), key=lambda x: x[1], reverse=(order == "desc")))

# 💲 Function to apply discount
def apply_discount(filtered):
    try:
        discount = float(input("\n💸 Enter discount percentage (e.g., 10 for 10%): "))
        for item in filtered:
            filtered[item] = round(filtered[item] * (1 - discount / 100), 2)
        print(f"✅ {discount}% discount applied to filtered items!")
    except ValueError:
        print("❌ Invalid input! Discount not applied.")

# 📤 Function to export results to a CSV file
def export_to_csv(filtered):
    filename = "filtered_items.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Price"])
        for item, price in filtered.items():
            writer.writerow([item, price])
    print(f"📁 Filtered items have been saved to '{filename}'.")

# 🟣 Main Program
def main():
    while True:
        print("\n📋 Menu:")
        print("1. Display all items")
        print("2. Add new items")
        print("3. Filter items by price")
        print("4. Exit")

        choice = input("\n👉 Enter your choice (1-4): ")

        if choice == "1":
            display_items()

        elif choice == "2":
            add_new_item()

        elif choice == "3":
            try:
                min_price = float(input("\n💰 Enter the minimum price to filter items: "))
                filtered_items = filter_items(min_price)

                if not filtered_items:
                    print("❌ No items found above this price.")
                    continue

                # Sorting option
                sort_choice = input("\n📊 Do you want to sort results? (yes/no): ").lower()
                if sort_choice == "yes":
                    order = input("🔼 Type 'asc' for ascending or 'desc' for descending: ").lower()
                    filtered_items = sort_items(filtered_items, order)

                # Display filtered items
                print("\n🟢 Filtered Items:")
                for item, price in filtered_items.items():
                    print(f"{item}: ${price}")

                # Apply discount
                if input("\n💲 Apply discount to these items? (yes/no): ").lower() == "yes":
                    apply_discount(filtered_items)

                # Export to CSV
                if input("\n📤 Export results to CSV? (yes/no): ").lower() == "yes":
                    export_to_csv(filtered_items)

            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        elif choice == "4":
            print("\n✈️ Thank you for using the Enhanced Flight Booking System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select a valid option.")

# 🚀 Run the program
main()


