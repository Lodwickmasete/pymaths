def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: The integer for which to calculate the factorial.

  Returns:
    The factorial of n, or 1 if n is 0.

  Raises:
    ValueError: If n is negative.
  """
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Get user input
num = int(input("Enter a non-negative integer: "))

# Calculate and print the factorial
try:
  result = factorial(num)
  print(f"The factorial of {num} is {result}")
except ValueError as e:
  print(e)