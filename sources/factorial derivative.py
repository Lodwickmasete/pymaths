import math

def find_factorial_derivative(num):
  """
  Finds the factorial whose derivative is the given number.

  Args:
    num: The number to check.

  Returns:
    The factorial whose derivative is the given number, or None if not found.
  """

  for i in range(1, num + 1):
    if math.factorial(i) == num:
      return f"{i}!"
  return None # No factorial found

while True: # This loop runs forever
  number = int(input("Enter a number: "))
  result = find_factorial_derivative(number)

  if result:
    print(f"The factorial whose derivative is {number} is {result}")
  else:
    print(f"There is no factorial whose derivative is {number}")