"""
Objective: Calculate the average of three numbers.
Instructions:
Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
Use the numbers 10,20,30 as input to functions
The function should return the average of these three numbers.
Expected Output:
The average of 10, 20, and 30 is 20.0
"""

#                                       ANSWER

def CalculateAverage(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    print(f"The average of {num1}, {num2}, and {num3} is {avg} ")


CalculateAverage(10, 20, 30)

