from app.discount import calculate_discount

price = 100
discount_percent = 20

result = calculate_discount(price, discount_percent)

print(f"Original price: {price}")
print(f"Discount: {discount_percent}%")
print(f"Final price: {result}")
