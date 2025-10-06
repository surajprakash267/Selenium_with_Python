"""
Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.
Instructions:
Create a class named BasicCalculator.
Define a constructor that initializes two numbers. Use numbers 10 & 5
Implement methods for:
Addition
Subtraction
Multiplication
Division
Each method should return the result of the operation.
Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
Example Output:
Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0
"""
#                               ANSWER

class BasicCalculator:

    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b

    def addition(self):
        return self.first_num + self.second_num

    def subtraction(self):
        return self.first_num - self.second_num

    def multiplication(self):
        return self.first_num * self.second_num

    def division(self):
        return self.first_num / self.second_num


# Creating an instance of the BasicCalculator class

calc = BasicCalculator(10, 5)

# Demonstration of  the functionality of each methods

print(f"Addition: {calc.first_num} + {calc.second_num} = {calc.addition()}")
print(f"Subtraction: {calc.first_num} - {calc.second_num} = {calc.subtraction()}")
print(f"Multiplication: {calc.first_num} * {calc.second_num} = {calc.multiplication()}")
print(f"Division: {calc.first_num} / {calc.second_num} = {calc.division()}")



