# Importing necessary modules
import math  # Standard math module
from math import factorial  # Importing specific function from math module
# Variables and Data Types

# Strings
greeting = "Hello, World!"  # A simple string
name = "Aboli"

# Integers and Floats
age = 21  # Integer
height = 5.8  # Float (decimal number)

# Booleans
is_student = True  # Boolean value

# Printing variables
print(greeting)
print("My name is", name)
print("I am", age, "years old.")
print("My height is", height, "feet.")

#  Basic Arithmetic Operations

# Addition, Subtraction, Multiplication, Division
sum_of_numbers = 5 + 3
difference = 10 - 2
product = 4 * 7
quotient = 16 / 4

print("Sum:", sum_of_numbers)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Modulus (remainder), Exponentiation (power)
remainder = 10 % 3
power = 2 ** 3

print("Remainder:", remainder)
print("2 to the power of 3:", power)

# Conditional Statements

# If-Else Example
if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is not an adult.")

# Elif Example
if age < 13:
    print(name, "is a child.")
elif age < 18:
    print(name, "is a teenager.")
else:
    print(name, "is an adult.")

# Loops

# For Loop Example
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While Loop Example
countdown = 5
print("Countdown:")
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrement countdown by 1

#  Functions

# Defining a function
def greet_user(username):
    """This function greets the user."""
    print("Hello,", username + "!")

# Calling the function
greet_user(name)

# Function with return value
def square(number):
    """This function returns the square of a number."""
    return number * number

result = square(4)
print("Square of 4 is:", result)

# Lists

# Creating and printing a list
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements to a list
fruits.append("orange")
print("Updated fruits list:", fruits)

# Looping through a list
print("List of fruits:")
for fruit in fruits:
    print(fruit)

#  Dictionaries

# Creating a dictionary
student = {
    "name": "Aboli",
    "age": 21,
    "is_student": True
}

# Accessing dictionary values
print("Student name:", student["name"])
print("Student age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("Updated student dictionary:", student)

# Looping through dictionary keys and values
print("Student details:")
for key, value in student.items():
    print(key, ":", value)

# Exception Handling
# Example of try-except block
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file handling example.")

#  Classes and Objects

# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing object properties and methods
print("Dog's name:", my_dog.name)
print("Dog's breed:", my_dog.breed)
my_dog.bark()

#Modules and Importing
# Using a function from the math module
print("Square root of 16 is:", math.sqrt(16))
# Using the factorial function from math module
print("Factorial of 5 is:", factorial(5))

#  List Comprehension
# Example of list comprehension
squares = [x ** 2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)
#  Sets
# Creating a set
numbers = {1, 2, 3, 4, 5}

# Adding an element to a set
numbers.add(6)
print("Updated set:", numbers)

# Removing duplicates from a list using a set
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique numbers:", unique_numbers)

#  Tuples
# Creating a tuple
coordinates = (10.0, 20.0)
# Accessing tuple elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])
#  Lambda Functions
# Example of a lambda function
double = lambda x: x * 2
print("Double of 5 is:", double(5))

#  Map Function

# Using map with a lambda function
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

#  Filter Function

# Using filter with a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#  Reduce Function

# Using reduce to sum a list of numbers
from functools import reduce

sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

#  Enumerate Function

# Using enumerate to get index and value in a loop
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#  Zip Function

# Using zip to combine two lists
colors = ["red", "yellow", "pink"]
fruits_and_colors = list(zip(fruits, colors))
print("Fruits and their colors:", fruits_and_colors)

#  Nested Loops
# Example of nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")

#  List Slicing

# Slicing a list
print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])

# Dictionary Comprehension

# Creating a dictionary using comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares_dict)

# String Formatting

# Using f-strings for formatting
formatted_string = f"My name is {name}, and I am {age} years old."
print(formatted_string)

# Reading user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
