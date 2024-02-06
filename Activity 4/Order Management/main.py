order=[]
def PlaceOrder(*items):
    for item in items:
        name, quantity, price = map(str, item.split(','))
        quantity = int(quantity)
        price = float(price)
        order.append({'name': name, 'quantity': quantity, 'price': price})
    print("Items added to the order successfully!\n")


def DisplayOrderDetails():
    print("\nOrder Details:")
    for item in order:
        total_cost = item['quantity'] * item['price']
        print(f"Item: {item['name']}, Quantity: {item['quantity']}, Total Cost: ${total_cost:.2f}")
    print()


def CalculateTotalCost():
    total=0
    for i in order:
        total+=(i['price']*i['quantity'])
    print(f"\nTotal Cost of the Order: ${total:.2f}\n")


def RemoveItems(*items):
    global order
    order = [item for item in order if item['name'] not in items]
    print("Items removed from the order.\n")




print("Welcome to the Restaurant Order Management System!\n")
print("1. Place Order\n2. Display Order Details\n3. Calculate Total Cost\n4. Remove Items from Order\n5. Exit")
while True:

    ch = int(input("Enter your choice: "))

    if ch == 1:
        items_input = input("Enter item details (name, quantity, price - comma-separated): ")
        PlaceOrder(items_input)
    elif ch == 2:
        DisplayOrderDetails()
    elif ch == 3:
        CalculateTotalCost()
    elif ch == 4:
        items_to_remove = input("Enter the item names to remove from the order: ")
        RemoveItems(items_to_remove)
    elif ch == 5:
        print("Exiting the Restaurant Order Management System. Goodbye!")
        break