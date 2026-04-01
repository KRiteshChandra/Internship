# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Avoid division error
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")

# Comparison operators
print("Is a equal to b?", a == b)
print("Is a greater than b?", a > b)

# Logical operators
if a > 0 and b > 0:
    print("Both numbers are positive")

# Assignment operator
a += 5
print("After adding 5 to a:", a)