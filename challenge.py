# Challenge: Write a Python program that asks the user to enter their name,
# their monthly salary amount, and the amount of bonus they received.
# The program should then print a message greeting the user by name
# and informing the salary amount in comparison with the received bonus.

# Bonus calculation: 1000 + salary * bonus_percentage

# 1) Ask the user to enter their name
name = input("Enter your name: ")

# 2) Ask the user to enter their salary amount
# Convert the input to a floating point number
salary = float(input("Enter your salary: "))

# 3) Ask the user to enter the bonus amount received
# Convert the input to a floating point number
bonus = float(input("Enter your bonus amount: "))

# 4) Calculate the final bonus value
calculated_bonus = 1000 + (salary * bonus)

# 5) Print the KPI calculation for the user
print(f"User {name} has a bonus of {calculated_bonus}.")

# 6) Print the personalized message including the user's name, salary, and bonus
print(f"Hello {name}, your salary is {salary}, and your bonus was {calculated_bonus}.")
