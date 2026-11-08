# Module 5, Problem 5

# Define main() function 
def main():

	# Prompt the user to enter last name
	last_name = input("Enter your last name: ")

	# Prompt the user to enter number of dependents
	dependents = int(input("Enter the number of dependents: "))

	# Prompt the user to enter gross income 
	gross_income = float(input("Enter gross income: $"))

	# Declare variable to store adjusted gross income 
	gross_adjusted = gross_income - (dependents * 12000)

	# Declare income tax rate variable 
	tax_rate = 0

	# Determine income tax rate 
	# If adjusted gross income > 50000,
	if (gross_adjusted > 50000):
		# income tax rate = 20%
		tax_rate = 0.20 
	# If adjusted gross income < 50000,
	elif (gross_adjusted <= 50000):
		# income tax rate = 10%
		tax_rate = 0.10

	# Calculate income tax = gross_adjusted * tax_rate 
	income_tax = gross_adjusted * tax_rate

	# If income tax < 0,
	if (income_tax < 0):
		# set income tax = 0
		income_tax = 100

	# Display output
	print("Last Name: " + last_name)
	print("Gross Income: $" + format(gross_income, ",.2f"))
	print("Number of Dependents: " + str(dependents))
	print("Adjusted Gross Income: $" + format(gross_adjusted, ",.2f"))
	print("Income Tax: $" + format(income_tax, ",.2f"))

# Call main() function
if __name__ == "__main__":
	main()

