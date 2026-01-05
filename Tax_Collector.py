def compute_tax(income):
    """
    Calculates the tax amount based on the given income using a graduated tax rate.

    Args:
        income (float): The person's income.

    Returns:
        float: The calculated tax amount, rounded to the nearest dollar.
               Returns None if the income is negative (due to data validation).
    """
    if income < 0:
        print("Error: Income cannot be negative.")
        return None

    tax = 0.0

    if income <= 5000:
        tax_rate = 0.00
    elif income <= 10000:
        tax_rate = 0.05
    elif income <= 20000:
        tax_rate = 0.105
    elif income <= 30000:
        tax_rate = 0.15
    else:
        tax_rate = 0.255

    tax = income * tax_rate
    return round(tax)

# Get income from the user
while True: # Keep asking until valid input is given
    try:
        income = float(input("Enter the person's income: $"))  # Get input and convert to float
        if income >= 0:
            break  # Exit the loop if income is valid
        else:
            print("Error: Income must be positive.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for income.")

# Calculate and display the tax
tax = compute_tax(income)
if tax is not None:
    print(f"Income: ${income}, Tax: ${tax}")

