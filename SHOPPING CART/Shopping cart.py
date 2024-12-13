def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Shopping Cart:")
        total_price = 0
        for item in cart:
            print(f"{item['name']}: {item['price']}")
            total_price += item['price']
        print(f"Total: ${total_price:.2f}")
        return total_price  # Return the total price 
def main():
    cart = []
    while True:
        print("\nShopping Cart Application")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Exit")
        print("5. Show total price")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item = {"name": item_name, "price": item_price}
            cart.append(item)
            print('Item added to cart!')

        elif choice == '2':
            display_cart(cart)

        elif choice == '3': # View cart
            if not cart:
                print("Your cart is already empty.")
            else:
                display_cart(cart)
                try:
                    item_index = int(input("Enter the item number to remove: ")) - 1
                    if 0 <= item_index < len(cart):
                        removed_item = cart.pop(item_index)
                        print(f"Removed item: {removed_item['name']}")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            print("Exiting the application.")
            break
        elif choice == '5':  # Show total price
            total = display_cart(cart)
            print(f"Total price: ksh.{total:.2f}")
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
