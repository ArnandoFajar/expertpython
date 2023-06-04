# If statement:
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# Example
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# You can also have an else without the elif:

# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# Example
# One line if statement:

if a > b:
    print("a is greater than b")
