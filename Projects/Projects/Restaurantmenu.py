#Define the menu of restaurant
menu = {
    'pizza':90,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Noodle':60,
    'French fries':40,
    'Coffee':80,
}

#Greet
print("Welcome to PY Restaurant")
print("Pizza:Rs90\nPasta:Rs50\nBurger:Rs60\nSalad:Rs70\nNoodle:Rs60\nFrench fries:Rs40\nCoffee:Rs80")

order_total = 0
#80 + 70 = 150
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not available!")

print(f"The total amount of item to pay is {order_total}")
            
