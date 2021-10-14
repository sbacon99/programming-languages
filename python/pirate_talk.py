# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random


# import translation document
f = open("Translation.txt")
lines = f.readlines()

# create dictionary
words = {}
for line in lines:
    translation = line.split(":")
    words[translation[0]] = translation[1].strip("\n")

# accept input
print()
print("Arr! Welcome to the pirate translator!")
val = input("Enter a line: ")

# translation
while val != "quit":                                        # stop on 'quit'
    for word in words:                                      # iterate through dictionary
        if word.find(" ") != -1:                            # if dictionary key has a space
            val = val.replace(word, words[word])            # replace string values if necessary 
        else:                                               # if dictionary key has no space
            valSplit = val.split(' ')                       # split string (this fixes bug in algorithm)
            for i in range(len(valSplit)):                  # iterate through 'valSplit'
                if word == valSplit[i]:                     
                    valSplit[i] = words[word]               # replace words if necessary
            val = ' '.join(valSplit)                        # rejoin string 

    
    if random.choice([1,2,3,4,5,6,7,8,9,10]) <= 3:          # add 'arr' to 30% of strings
         print(val + ", arr.")
    else:
         print(val)
   
    val = input("Enter a line: ")                           # accept next input

    

    