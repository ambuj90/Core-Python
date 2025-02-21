# 🛒 Inventory Dictionary
inventory = {"Apples": 20, "Bananas": 15, "Oranges": 10, "Mangoes": 5, "Grapes": 8}

# 🛍️ Purchase Function
def purchase(product, quantity):
    if product in inventory:
        if inventory[product] >= quantity:
            inventory[product] -= quantity
            print(f"✅ Purchased {quantity} {product}. Stock left: {inventory[product]}")
            if inventory[product] <= 5:
                print(f"⚠️ Low stock alert for {product}!")
        else:
            print(f"❌ Not enough {product}. Only {inventory[product]} available.")
    else:
        print(f"❌ {product} not found in inventory.")

# 📦 Display Inventory
print("\n📦 Inventory:", inventory)

# 🛒 Example Purchases
purchase("Apples", 5)
purchase("Mangoes", 3)
purchase("Oranges", 12)

# 📦 Final Inventory
print("\n📦 Updated Inventory:", inventory)


