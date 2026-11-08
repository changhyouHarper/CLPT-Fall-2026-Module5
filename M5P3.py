# Moduble 5, Problem 3

# Define main() function 
def main(): 

	# Prompt the user to enter number of books 
	numBooks = int(input("Enter the number of books: "))

	# Prompt the user to enter cost per book 
	cost = float(input("Enter the cost of the book: $"))

	# Declare variable to calculate subtotal (without shipping fees)
	subtotal = numBooks * cost 

	# Declare variable to store shipping fees 
	shippingRate = 0

	# If cost > $50, 
	if (subtotal > 50):
		# Shipping is free 
		shippingRate = 0
	# If cost < $50,
	else:
		shippingRate = 25

	# Declare variable to store total 
	total = subtotal + shippingRate

	# Display output
	print("Order Subtotal: $" + format(subtotal, ".2f"))
	print("Shipping Charge: $" + format(shippingRate, ".2f"))
	print("Order Total: $" + format(total, ".2f"))

# Call main() function
if __name__ == "__main__":
    main()