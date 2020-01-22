# Author: Jonas  Toussaint
# Class: CEN 4213
# Assignment: 2
# Due: 1/21/2020 

# Get User to input 5 numbers
N1 = int(input("Enter first number: "))
N2 = int(input("Enter second number: "))
N3 = int(input("Enter third number: "))
N4 = int(input("Enter fourth number: "))
N5 = int(input("Enter fifth number: "))

lst = [N1, N2, N3, N4, N5]

# sorting the list
lst.sort()

# Print Ouput 
print("Of the 5 numbers inputted", lst, lst[-1], " is largest\n")

print("Of the 5 numbers inputted", lst, *lst[:1], " is smallest")

