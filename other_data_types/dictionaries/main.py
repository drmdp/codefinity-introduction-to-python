# product ID and category
grocery_inventory = {
"Milk": (113, "Dairy"),
"Eggs": (116, "Dairy"),
"Bread": (117, "Bakery"),
"Apples": (141, "Produce")
}
bread_details = grocery_inventory.get("Bread")
print("Details of bread:", bread_details)
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adfding Cookies:", grocery_inventory)
removed_item = grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)
