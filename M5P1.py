# Module 5, Problem 1 

# Define main() function  
def main(): 

	# Declare variable to store unit price
	unit_price = 0

	# Prompt the user to enter quantity of an item 
	item_quantity = int(input("Enter the quantity of an item: "))

	# If quantity >= 1000 ... 
	if (item_quantity >= 1000):
		# unit price = $3.00
		unit_price = 3.00
	# If quantity < 1000 ... 
	elif (item_quantity < 1000):
		unit_price = 5.00

	# Declare variable to store extended price calculation
	extended_price = item_quantity * unit_price

	# Declare variable and store tax rate 
	tax_rate = 0.07
	tax = tax_rate * extended_price

	# Declare variable to store the final total  
	total = extended_price + (tax_rate * extended_price)

	# Display output
	print("Item Quantity: " + str(item_quantity))
	print("Unit Price: $" + format(unit_price, ".2f"))
	print("Extended Price: $" + format(extended_price, ".2f"))
	print("Tax Amount: $" + format(tax, ".2f"))
	print("Total: $" + format(total, ".2f"))

# Call main() function
if __name__ == "__main__":
    main()





