products = {
    "Apple":125,
    "Bannana":45,
    "Grapes":60,
    "Mango":800,
    "Orange":90
}

# Display the available products:
def displayAvailableProducts():
    print("Available Products are: \n")

    for product, price in products.items():
        print(f"Product: {product}, Price: ${price}/kg")

# Add a new product to cart:
def addProduct(cart):
    name=input("Enter product name: ")

    if(name not in products.keys()):
        return print(f"Product with {name} does not exist")

    cart.append(name)

    print("Product added successfully!")

# Display the products in cart:
def displayCart(cart):
    if len(cart) == 0:
        print("Shopping cart is empty!")
        return

    print("Shopping cart Contents:")
    
    for item in cart:
        print(f"Product: {item}, Price: ${products[item]}/kg")

# Remove an item from cart:
def removeProduct(cart):
    item = input("Enter the product name to remove: ")
    
    try:
        if item in cart:
            cart.remove(item)
            print(f"{item} was removed from the cart")
        else: raise Exception(f"No product with name {item} in the cart")
    except Exception as err:
        print(str(err))

# Calculate the total price:
def calcTotalPrice(cart):
    totalPrice = 0
    
    for item in cart:
        totalPrice+=products[item]
    
    print(f"Total Price: ${totalPrice}")

# Checkout:
def checkout(cart):
    print("The checkout details are: ")

    displayCart(cart)
    calcTotalPrice(cart)
    cart.clear()

def main():
    # Shoping List:
    cart=[]
    print("Welcome to the online shoping cart!")
    print("\n0. Display Available Products")
    print("\n1. Add product")
    print("\n2. Display Cart")
    print("\n3. Remove Product")
    print("\n4. Calculate Total Price")
    print("\n5. Checkout")
    print("\n6. Exit")

    while(True):
        choice=int(input("\nEnter your choice:"))
        if choice==0:
            displayAvailableProducts()
        elif choice==1:
            addProduct(cart)
        elif choice==2:
            displayCart(cart)
        elif choice==3:
            removeProduct(cart)
        elif choice==4:
            calcTotalPrice(cart)
        elif choice==5:
            checkout(cart)
        elif choice==6:
            exit()
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    main()