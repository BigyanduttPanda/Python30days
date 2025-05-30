#Create an inventory system tracking items and quantities with a dictionary
# - Add Items
# - Remove Items
# - Display current inventory

# Inventory Dictionary
Inventory = {"item_1": 10, "item_2": 5, "item_3": 15}

# Add items
def add_item(item, quantity):
    if item in Inventory:
        Inventory[item] += quantity
        print(f"Added {quantity} of {item}. New quantity: {Inventory[item]}.")
    else:
        Inventory[item] = quantity
        print(f"Added new item: {item} with quantity {quantity}.")

# Remove items
def remove_items(item, quantity):
    if item in Inventory and Inventory[item] >= quantity:
        Inventory[item] -= quantity
        print(f"Removed {quantity} of {item}. Remaining quantity: {Inventory[item]}.")
        if Inventory[item] == 0:
            del Inventory[item]   # Remove item if quantity reaches zero
            print(f"{item} has been removed from inventory.")
    else:
        print("Item is not present in the inventory")

# Display Inventory
def display_inventory():
    print("Current Inventory:")
    for item, quantity in Inventory.items():
        print(f"{item}: {quantity}")

# Example
add_item("item_4", 25)
remove_items("item_2", 2)
display_inventory()
