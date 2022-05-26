
import sales.shopping_cart,sales.shopping_order


cart = sales.shopping_cart.Cart()
order = sales.shopping_order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = sales.shopping_order.Order()
    order.get_input()


cart_message = "Items in your Cart.."
print(cart_message)
print('-' * len(cart_message))
print("{:<10} {:<10}".format('Items', 'Quantity'))
for key in cart._contents:
    items,quantity = key,cart._contents[key]
    print("{:<10} {:<10}".format(items,quantity))