# Python Automation Tools

## Project Overview
Collection of Python utility applications designed to automate common financial and business calculations. These tools demonstrate proficiency in Python programming, input validation, error handling, and user interface design for practical real-world scenarios.

## Technologies Used
- **Language:** Python 3.x
- **Concepts:** Functions, conditional logic, loops, exception handling, user input validation
- **Development Environment:** Python IDE/Terminal

## Projects Included

### 1. Tax Calculator (`Tax_Collector.py`)
Automated tax computation tool that calculates tax liability based on graduated income brackets.

**Features:**
- **Graduated tax rate calculation** based on income thresholds:
  - $0 - $5,000: 0% tax rate
  - $5,001 - $10,000: 5% tax rate
  - $10,001 - $20,000: 10.5% tax rate
  - $20,001 - $30,000: 15% tax rate
  - $30,001+: 25.5% tax rate
- **Robust input validation** prevents negative income values
- **Error handling** catches non-numerical inputs and prompts user to retry
- **User-friendly interface** with clear prompts and formatted output
- **Automated rounding** to nearest dollar for practical results

**Real-world application:** Similar to payroll systems, tax filing software, and financial planning tools that require accurate graduated tax calculations.

### 2. Additional Tools
*(Future additions: Stock trading calculator, sales tax calculator, currency converter)*

## Code Highlights

### Input Validation with Exception Handling
```python
while True:
    try:
        income = float(input("Enter the person's income: $"))
        if income >= 0:
            break
        else:
            print("Error: Income must be positive.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for income.")
```

**Why this matters:** Production applications must handle invalid user input gracefully without crashing—a critical skill for any software development role.

### Function Design with Documentation
```python
def compute_tax(income):
    """
    Calculates the tax amount based on the given income using a graduated tax rate.
    
    Args:
        income (float): The person's income.
    
    Returns:
        float: The calculated tax amount, rounded to the nearest dollar.
    """
```

**Best practice demonstrated:** Clear docstrings make code maintainable and professional, following Python PEP 257 documentation standards.

## Skills Demonstrated

**Programming Concepts:**
- Function design and modular code structure
- Conditional logic (if/elif/else statements)
- Loop control (while loops with break conditions)
- Exception handling (try/except blocks)
- Data type conversion and validation
- String formatting for user output

**Software Development Practices:**
- Input validation and error handling
- User experience design (clear prompts and error messages)
- Code documentation with docstrings
- Edge case handling (negative numbers, non-numeric input)
- DRY principle (Don't Repeat Yourself) through function reusability

## How to Run

1. **Clone the repository:**
```bash
   git clone https://github.com/aspivey22/python-automation-tools.git
   cd python-automation-tools
```

2. **Run the tax calculator:**
```bash
   python Tax_Collector.py
```

3. **Enter income when prompted:**
```
   Enter the person's income: $25000
   Income: $25000.0, Tax: $3750
```

## Technical Decisions

**Why graduated tax rates?**  
Real-world tax systems use progressive brackets—this project simulates actual tax calculation logic used in payroll systems and financial software.

**Why round to nearest dollar?**  
Financial applications typically display currency in whole dollars for clarity, matching standard accounting practices.

**Why loop for input validation?**  
Prevents program crashes from invalid input while maintaining a smooth user experience—essential for production-ready applications.

## What I Learned

This project reinforced:
- **Error handling is non-negotiable:** User input is unpredictable; robust validation prevents crashes and improves UX
- **Functions improve code reusability:** The `compute_tax()` function can be easily imported and used in other projects
- **Documentation matters:** Clear docstrings make code maintainable for future developers (including future me!)

## Future Enhancements

Planned additions:
- [ ] Stock trading profit/loss calculator with buy/sell prices
- [ ] Sales tax calculator for multiple jurisdictions
- [ ] Currency conversion tool with real-time exchange rates
- [ ] GUI interface using Tkinter
- [ ] Unit tests for tax calculation accuracy
- [ ] Export results to CSV for record-keeping

## Contact

**Ar'Jah'Naye Spivey**
- LinkedIn: [linkedin.com/in/aspivey22](https://linkedin.com/in/aspivey22)
- Email: sarjahnaye@gmail.com
- GitHub: [github.com/YOUR_USERNAME](https://github.com/aspivey22)

---

*Project completed: April 2025*  
*Part of Computer Information Systems coursework demonstrating practical Python programming skills*
