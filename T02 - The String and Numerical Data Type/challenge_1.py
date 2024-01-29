# Import math library
import math

# Ask the user to enter the lengths of all three sides of a triangle.
#a = 8.0       # Test Data
#b = 5.0       # Test Data
#c = 5.0       # Test Data
a = float(input("Enter length of Side 1 : "))
b = float(input("Enter length of Side 2 : "))
c = float(input("Enter length of Side 3 : "))

# Calculate the area of the triangle and print
s = (a+b+c)/2
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("Area = " + str(area))