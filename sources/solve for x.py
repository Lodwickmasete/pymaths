import re

def solve_equation(equation):
  try:
    # Extract variable and coefficients using regular expressions
    match = re.match(r'(-?\d*)x\s*([-+]\s*\d+)\s*=\s*(-?\d+)', equation)
    if match:
      coefficient = int(match.group(1) or 1) # If no coefficient, it's 1
      constant_left = int(match.group(2))
      constant_right = int(match.group(3))

      # Solve for x
      x = (constant_right - constant_left) / coefficient
      return f"x = {x}"
    else:
      return "Invalid equation format. Please use format 'ax + b = c'"
  except Exception as e:
    return f"Error: {e}"

# Get input equation from the user
equation = input("Enter the equation (e.g., 2x - 3 = 25): ")

# Solve the equation and print the result
solution = solve_equation(equation)
print(solution)