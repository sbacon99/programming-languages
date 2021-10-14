#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python functional programming classwork
3/17/2021
Ryan Mattfeld AND Elizabeth von Briesen

"""

import functools

# Create and test a solution to solve the following problems using
# functional programming:
    
strs = ["elon", "mascot", "phoenix", "clemson", "has", "tiger"]
ints = [5, 17, 7, 2, 4, 15, 90]
print()

# Problem 1: Given a list of Strings, create and print a list of strings, but
# omit any that contain an 'a'. EX) given the inputs in "strs" above, the result
# should be a list with ["Elon", "Phoenix", "Clemson", "Tiger"] - Print your result to test

print("Problem 1")

strsNoA = list(filter(lambda x: "a" not in x, strs))

print(strsNoA)
print()

# Problem 2: Given a list of Strings, first append an 'i' to the end,
# then remove any strings that contain the substring 'ni'.

print("Problem 2")

def addi(x):        
	return x + "i"

strsNoni = list(filter(lambda x: "ni" not in x, list(map(addi, strs))))

print(strsNoni)
print()

# Problem 3: Given a list of integers, create and print a list with all
# "teens" removed (teens are any numbers between 13 and 19)

print("Problem 3")

numsNoTeen = list(filter(lambda x: x < 13 or x > 19, ints))

print(numsNoTeen)
print()

# Problem 4: Given a list of integers, remove any with two or more digits.
# Then, sum the squares of all remaining numbers and add the product to 42.
# (In the 'ints' list provided, the correct answer should be 42+25+49+4+16 = 136

print("Problem 4")

def two_less(x): # filter
    return len(str(x)) < 2
def square(x): # map
    return x*x
def add(x, y):    	 
	return x + y    

intSquareSum = 42 + functools.reduce(add, list(map(square, list(filter(two_less, ints)))))

print(intSquareSum)
print()

# Problem 5: Given a list of Strings, create and print a list of strings by first
# removing any with lengths between 4 and 6 (inclusive), then add a "z" after the
# first letter of each remaining word.

print("Problem 5")

def length(x):
    return len(x) < 4 or len(x) > 6
def addz(x):
    return x[0] + "z" + x[1:]

wordz = list(map(addz, list(filter(length, strs))))

print(wordz)
print()

# Problem 6: Given a list of integers, create and print a list of each of the
# numbers multiplied by 3, removing any of the resulting values that end in 1.

print("Problem 6")

def mult(x):
    return x*3

intsNoOne = list(filter(lambda x: x % 10 != 1, list(map(mult, ints))))

print(intsNoOne)
print()

# Problem 7: Given a collection of integers, remove any that end in 7, then
# add together each of the remaining numbers plus an additional 2 every time
# a pair of numbers is added.
# EX: From the list above, after numbers ending in 7's are removed, the remaining
# values would be [5,2,4,15,90]. The math requested for this problem would result in:
# (5 + 2 + 2) # given that the first two values are 5 ans 2, add them plus 2
# (9 + 4 + 2) # Given 11 from the prior sum, add 4 plus 2 extra
# (15 + 15 + 2)// Given 17 from the prior sum, add 15 plus 2 extra
# (32 + 90 + 2)// Finally, add 90 plus 2 to the running sum to get the result of 124
# HINT: This is a relatively easy operation - the whole process can be accomplished with
# two function calls.

print("Problem 7")

def noSeven(x):
    return x % 10 != 7
def add_2(x, y):    	 
	return x + y + 2 

sumTwos = functools.reduce(add_2, list(filter(noSeven, ints)))
print(sumTwos)





