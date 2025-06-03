# Challenge: Write a Python program that asks the user to enter their name,
# their monthly salary amount, and the amount of bonus they received.
# The program should then print a message greeting the user by name
# and informing the salary amount in comparison with the received bonus.

# Bonus calculation: 1000 + salary * bonus_percentage

# 1) Ask the user to enter their name
user_name = input("Enter your name: ")

# 2) Ask the user to enter their salary amount
# Convert the input to a floating point number
monthly_salary = float(input("Enter your monthly salary (positive number, e.g., 2000): "))

# 3) Ask the user to enter the bonus amount received
# Convert the input to a floating point number
bonus_percentage = float(input("Enter your bonus percentage as a decimal (e.g., 0.10 for 10%): "))

# 4) Calculate the final bonus value
bonus_value = 1000 + (monthly_salary * bonus_percentage)

# 5) Print the personalized message including the user's name, salary, and bonus
print(f"Hello {user_name}, your salary is R$ {monthly_salary:.2f} and your bonus is R$ {bonus_value:.2f}.")

