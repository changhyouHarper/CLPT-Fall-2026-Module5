# Module 5, Problem 4

# Define main() function
def main():

	# Prompt user to enter the name of the appliance
	appliance = input("Enter the name of the appliance: ")

	# Prompt user to enter the cost of an appliance
	cost = float(input("Enter the cost of the appliance: $"))

	# Define and declare warranty cost variable 
	warranty = 0

	# If cost of appliance > $1,000, 
	if (cost > 1000):
		# warranty cost is 10%
		warranty = 0.10 
	# If cost of appliance < $1,000,
	elif (cost < 1000):
		# warranty cost is 5%
		warranty = 0.05

	# Calculate warranty total 
	warranty_total = cost * warranty

	# Calculate total 
	total = cost + warranty_total

	# Display output
	print("Appliance Name: " + appliance)
	print("Appliance Cost: $" + format(cost, ".2f"))
	print("Warranty Cost: $" + format(warranty_total, ".2f"))
	print("Total: $" + format(total, ".2f"))

# Call main() function
if __name__ == "__main__":
	main()