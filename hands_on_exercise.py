"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi), pi)



# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if(i<50):
    print("i is less than 50")
elif (i>50):
    print("i is greater than 50")
        


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print("My fruit is ", picked_fruit)
if(picked_fruit=="orange"):
    print("Color of my Fruit is Orange")
elif(picked_fruit=="strawberry"):
    print("Color of my fruit is Red")
elif(picked_fruit=="banana"):
    print("Color of my fruit is Yellow")

        

        


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
def multiplies(a,b):
    result = a*b
    return result
print("Multiplication of a and b =", multiplies(a,b))




# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiplies(12,96))

print("48 x 17 =",multiplies(48,17))

print("196523 x 87323 =",multiplies(196523,87323))