print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
orders = {}
user_input = input("> ").strip().lower()
while user_input != "quit":
  orders[user_input] = orders.get(user_input, 0) + 1
  order_text = "orders" if orders[user_input] > 1 else "order"
  print(f"\n** {orders[user_input]} {order_text} of {user_input.capitalize()} has been added to your meal **\n")
  user_input = input("> ").strip().lower()
else:
  print(f"\nYour order:")
  for key, value in orders.items():
    print(f"{key.capitalize()}: {value}")
  print("Thank you for purchasing from the Snakes Cafe. Enjoy your day!")