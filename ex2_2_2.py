# The total wholesale cost

cover_price = 24.95
discount = 0.4 
basic_shipping_fee = 3
additional_shipping_fee = 0.75
copies = 60

total_cost = (cover_price * discount * copies) + (basic_shipping_fee + (copies - 1) * additional_shipping_fee)

print('The total wholesale cost is {}'.format(round(total_cost, 2)))
