PRICE = 3.49
DISCOUNT = 0.6

loaves = int(input("Number of loaves of day old bread: "))
regular_price = PRICE * loaves
discount = regular_price * DISCOUNT
total_price = regular_price - discount
print("Regular price: ${:6.2f}".format(regular_price))
print("     Discount: ${:6.2f}".format(discount))
print("  TOTAL PRICE: ${:6.2f}".format(total_price))
