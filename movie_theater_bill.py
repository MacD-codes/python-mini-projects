menu = {
    "popcorn": 300.00,
    "pizza": 250.00,
    "nachos": 250.00,
    "fries": 150.00,
    "chips": 100.00,
    "soda": 200.00,
    "juice": 150.00
}
cart = []
total = 0
print("--------------- MENU ---------------")
for key, value in menu.items():
    print(f"{key:10}: Rs.{value:.2f}")
print("------------------------------------")

while True:
    food=input("Select an item(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------------- BILL ---------------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: Rs. {total:.2f}")
print()
print("------------------------------------")
