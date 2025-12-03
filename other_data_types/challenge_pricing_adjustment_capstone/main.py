#Pricing Adjustment Capstone
grocery_inventory = {
    "Milk":("Dairy", 3.50, 8), 
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
category, price, stock = grocery_inventory["Eggs"]
eggs_price = grocery_inventory["Eggs"][1]
print(eggs_price)
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, price - 1, stock)
    print("New Eggs Price", grocery_inventory["Eggs"][1])
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(grocery_inventory)