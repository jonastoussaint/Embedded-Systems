'''
Author: Jonas Toussaint

Assignment: CEN4213_Assign3_S20

Objective: Write a program that takes number of ounces given and converts the
input to pounds, grams and kilograms then displays it to the screen. Assume that the given
ounces is an integer. (anything else should be considered error handling and treated
accordingly)

Due Date: 1/23/2020
'''
lb = 0
g = 0
kg = 0

oz = int(input("Enter the number of ounces: "))
print("The number you entered is ", oz)

lb = oz * (0.062499949018125)
g = oz * (28.3495)
kg = oz * (0.0283495)

print("The number of pounds = ", round(lb, 2))
print("The number of grams = ", round(g, 2))
print("The number of kilograms = ", round(kg, 2))
