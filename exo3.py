total_amount = float(input("Enter the total amount of the purchase: "))
num_items = int(input("Enter the number of items: "))
day_of_week = input("Enter the day of the week: ").lower()


if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount = 0.10 
elif day_of_week in ["saturday", "sunday"]:
    discount = 0.20  

if num_items > 5:
    discount += 0.05


final_price = total_amount * (1 - discount)

print(f"The total price after applying the discount is: ${final_price:.2f}")
