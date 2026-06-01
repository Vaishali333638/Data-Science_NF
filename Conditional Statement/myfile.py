#Write a program to check whether a year is a leap year or not.
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 

#Write a program to find the largest among three numbers using nested conditional statements.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is the largest number.")
elif (num2 >= num1) and (num2 >= num3):
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.") 

#Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character.
char = input("Enter a character:")
if char.isupper():
    print(f"{char} is an uppercase letter.")
elif char.islower():
    print(f"{char} is an lowercase letter.")
elif char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is a special character.")

#Write a program to calculate electricity bill using different unit slabs.
units = float(input("Enter the number of units consumed:"))
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
print(f"Total electricity bill :{bill} rupees.")

#Write a program to determine whether a triangle is equilateral, isosceles, or Scalene.
side1 = float(input("Enter the first side:"))
side2 = float(input("Enter the second side:"))
side3 = float(input("Enter the third side:"))
#Conditinal statements 
if (side1 == side2 == side3):
    print("The triangle is Equilateral.")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")

#Write a program to create a simple calculator using if-elif-else.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
#User se operation input lena
print("Select operation: +,-,*,/")
operation = input("Enter operation:")
#conditinal statements for calculator
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation.")

#Write a program to calculate income tax according to salary ranges.
salary = float(input("Enter your salary:"))
if salary <= 300000:
    tax = 0
elif salary <= 600000:
    tax = (salary - 300000) * 0.05
elif salary <= 900000:
    tax = (300000 * 0.05) + (salary - 600000) * 0.10
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (salary - 900000) * 0.20
print(f"your income tax is: {tax} rupees.")

#Write a program to check login authentication using username and password conditions.
username = input("Enter username:")
password = input("Enter password:")
#predefined username and password
predefined_username = "admin"
predefined_password = "password123"
#conditional statements for authentication
if username == predefined_username and password == predefined_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
    

#Write a program to determine whether a point lies in first quadrant, second quadrant, third quadrant, fourth quadrant, On axis, or At origin.
x = float(input("Enter x coordinate:"))
y = float(input("Enter y coordinate:"))
if x > 0 and y > 0:
    print("The point lies in the first quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the second quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the third quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the fourth quadrant.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
else:
    print("The point lies on the axis.")

#Write a program to assign grades based on marks and display distinction for high scores.
marks = float(input("Enter your marks:"))
if marks >= 90:
    grade = "A"
    distinction = "Distinction"
elif marks >= 80:
    grade = "B"
    distinction = "Distinction"
elif marks >= 70:
    grade = "C"
    distinction = "No Distinction"
elif marks >= 60:
    grade = "D"
    distinction = "No Distinction"
else:
    grade = "F"
    distinction = "No Distinction"
print(f"Your grade is" f"{grade} and {distinction}.")
