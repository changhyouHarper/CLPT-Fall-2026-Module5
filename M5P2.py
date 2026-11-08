# Module 5, Problem 2 

# Define the main() function
def main():

	# Declare the unit price variable 
	unit_price = 0

	# Prompt the user to enter for an item
	item = input("Enter an item: ")

	# Prompt the user to enter a quantity 
	quantity = int(input("Enter the quantity of the item: ")) 

	# If item == "A",
	if (item == "A"):
		# unit price == 10 
		unit_price = 10 
	# if item == "B",
	elif (item != "A"):
		# unit price == 20
		unit_price = 20

	# Declare variable to store extended price calculation
	extended_price = quantity * unit_price

	# Display output
	print("Item: " + item)
	print("Unit Price: $" + format(unit_price, ".2f"))
	print("Extended Price: $" + format(extended_price, ".2f"))

# Call main() function
if __name__ == "__main__":
    main()

