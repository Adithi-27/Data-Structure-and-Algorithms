# -*- coding: utf-8 -*-
"""02-Variables.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oUKfAFN-du4GoqoGpIt5AoDXdVZDOBHx
"""

a=100

## Declaring And Assigning Variables

age=24
height=5.5
name="Adithi"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)

## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="Adithi"
last_name="Roy"

## case sensitivity
name="Adithi"
Name="Roy"

## Understnading Variable types
## Python is dynamically typed,type of a variable is determined at runtime
age=25 #int
height=5.5 #float
name="Adithi" #str
is_student=True #bool

print(type(name))

## Type Checking and Conversion

type(height)

age=25
print(type(age))

# Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))

age='25'
print(type(int(age)))

name="Adithi"
int(name)

height=5.11
type(height)

float(int(height))

## Dynamic Typing
## Python allows the type of a vraible to change as the program executes
var=10 #int
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))

## input

age=int(input("What is the age"))
print(age,type(age))

### Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

