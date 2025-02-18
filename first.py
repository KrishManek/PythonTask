# Writing the first Python program
print("Hello, World!")  # This prints "Hello, World!" to the console

# This is a single-line comment

"""
This is a multi-line comment 
spanning multiple lines.
"""

'''
Another way to write multi-line comments.
'''

# Docstring example
"""This is a docstring explaining the purpose of this script."""

# Input and Output
user_input = input("Enter something: ")
print("You entered:", user_input)  

a = 5       
b = 3.14    
c = "Hello" 
d = True    


print(type(a), type(b), type(c), type(d))

# Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Comparison Operators
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical Operators
a = True
b = False
print("Logical AND:", a and b)
print("Logical OR:", a or b)
print("Logical NOT:", not a)

# Bitwise Operators
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left shift:", x << 1)
print("Right shift:", x >> 1)

# Identity Operators
a = 10
b = 10
print("Identity 'is':", a is b)
print("Identity 'is not':", a is not b)

# Membership Operators
list_example = [1, 2, 3, 4, 5]
print("Membership 'in':", 3 in list_example)  # True
print("Membership 'not in':", 6 not in list_example)  # True