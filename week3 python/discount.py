# Function to calculate the discount
def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    final_price = price - (price * discount_percent / 100)
    return final_price
  else:
   return price

# Prompting user input
try:
    # Get the original price and discount percentage from the user
    price = float(input("Enter price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price 
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")
except ValueError:
    print("Invalid input. Please enter number values for the price and discount of the item.")
