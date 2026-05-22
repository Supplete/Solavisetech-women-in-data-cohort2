a=10
b=16

# Addition operator
c=a+b
print(c)

# Subtraction operator
d=b-a
print(d)

#Multiplication operator
e=a*b
print(e)

#Division operator
f=b/a
print(f)

#Modulus operator
g=b%a
print(g)


#Area of shapes
#Area of a rectangle
Length=5
Width=3
Area_of_rectangle=Length*Width
print("Area of rectangle is", Area_of_rectangle)


#Area of a triangle
Base=4
Height=6
Area_of_triangle=0.5*Base*Height
print("Area of triangle is", Area_of_triangle)

#Area of a circle
import math
Radius=7
Area_of_circle=math.pi*Radius**2
print("Area of circle is", Area_of_circle)

#Number is Even or Odd
number=int(input("Enter a number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")

#Calculate the percentage grade of students

total_marks=int(input("Enter total marks:"))
marks=int(input("Enter your marks:"))
percentage=(marks/total_marks)*100
print("Percentage grade is", percentage)

#BMI Calculator
weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in meters:"))
BMI=weight/(height**2)
print("Your BMI is", BMI)

#power operator
base=int(input("Enter the base number:"))
exponent=int(input("Enter the exponent:"))
power=base**exponent
print("The result of", base, "raised to the power of", exponent, "is", power)

#Modulus operator
dividend=int(input("Enter the dividend:"))
divisor=int(input("Enter the divisor:"))
remainder=dividend%divisor
print("The remainder of", dividend, "divided by", divisor, "is", remainder)