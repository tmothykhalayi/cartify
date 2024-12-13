from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# ShoppingCart class definition
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item_name, price):
        """Add an item to the shopping cart."""
        self.cart.append({"name": item_name, "price": price})

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        return sum(item['price'] for item in self.cart)

# ShoppingCartApp definition
class ShoppingCartApp(App):
    def build(self):
        self.cart = ShoppingCart()
        self.layout = BoxLayout(orientation="vertical")
        
        # Title Label
        self.label = Label(text="Shopping Cart App", font_size='40sp', size_hint_y=0.2)
        self.layout.add_widget(self.label)
        
        # Input for Item Name
        self.item_name_input = TextInput(hint_text="Item Name", size_hint_y=0.4)
        self.layout.add_widget(self.item_name_input)
        
        # Input for Item Price
        self.item_price_input = TextInput(hint_text="Item Price", size_hint_y=0.2, input_filter="float")
        self.layout.add_widget(self.item_price_input)
        
        # Add Item Button
        self.add_button = Button(text="Add Item", size_hint_y=0.1)
        self.add_button.bind(on_press=self.add_item)
        self.layout.add_widget(self.add_button)
        
        # View Cart Button
        self.view_cart_button = Button(text="View Cart", size_hint_y=0.1)
        self.view_cart_button.bind(on_press=self.view_cart)
        self.layout.add_widget(self.view_cart_button)
        
        # Display Cart Contents
        self.cart_label = Label(text="", size_hint_y=0.6)
        self.layout.add_widget(self.cart_label)
        
        return self.layout

    def add_item(self, instance):
        """Add item to the cart and display a message."""
        item_name = self.item_name_input.text
        try:
            price = float(self.item_price_input.text)
            self.cart.add_item(item_name, price)
            self.label.text = f"Added {item_name} for {price:.2f}"
            self.item_name_input.text = ""
            self.item_price_input.text = ""
        except ValueError:
            self.label.text = "Error: Enter a valid price."

    def view_cart(self, instance):
        """View cart items and total price."""
        if not self.cart.cart:
            self.cart_label.text = "Your cart is empty."
        else:
            items = "\n".join([f"{item['name']} - {item['price']:.2f}" for item in self.cart.cart])
            total = self.cart.calculate_total()
            self.cart_label.text = f"Items:\n{items}\n\nTotal: {total:.2f}"

if __name__ == "__main__":
    ShoppingCartApp().run()
