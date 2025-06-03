#Exercise 01: Remove spaces from the name to count only the letters

name = input("Enter your name: ").replace(" ", "")
print(f"Your name has {len(name)} letters.")

#Exercise 02: Ask the user to input two numbers and return their sum

value_01 = int(input("Enter the first number: "))
value_02 = int(input("Enter the second number: "))

result = value_01 + value_02
print(f"The sum of the two numbers is {result}.")