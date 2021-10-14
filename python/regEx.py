# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Part 1: List Comprehensions
print("Part 1: List Comprehensions")
print()

firstSentence = ["Help", "me", "stack", "overflow", "you're", "my", "only", "hope"]
secondSentence = ["I", "hope", "you're", "enjoying", "the", "riddles", "I've", "created"]

# Question 1
print("Question 1")
print([x for x in firstSentence+secondSentence if len(x) > 4 ])
print()

# Question 2
print("Question 2")
print([x for x in firstSentence+secondSentence if x[0] == 'o'])
print()

# Question 3
print("Question 3")
print([x[-3:] for x in firstSentence])
print()

# Question 4
print("Question 4")
print([x for x in firstSentence+secondSentence if len(x) % 2 == 1])
print()

# Question 5
print("Question 5")
print([secondSentence.index(x) for x in secondSentence if len(x) % 2 == 1])
print()

# Question 6
print("Question 6")
print([x for x in firstSentence+secondSentence if  x.find('y') != -1])
print()

# Question 7
print("Question 7")
print([x for x in firstSentence for y in secondSentence if len(x) == len(y) and firstSentence.index(x) == secondSentence.index(y)])
print()

# Question 8
print("Question 8")
print([x for x in firstSentence if x in secondSentence])
print()

# Question 9
print("Question 9")
print([x[0].upper() + x[1:] for x in firstSentence])
print()

# Question 10
print("Question 10")
print([x.replace('o', 'aa') for x in firstSentence])
print()

# Question 11
print("Question 11")
print([(x,y) for x in firstSentence[-4:] for y in secondSentence[-4:] if firstSentence.index(x) == secondSentence.index(y)])
print()

# Question 12
print("Question 12")
print([(x,y) for x in firstSentence for y in secondSentence if x == y])
print()

# Question 13
print("Question 13")
print([(x + y) for x in firstSentence for y in secondSentence if len(x) > len(y)])
print()

# Question 14
print("Question 14")
print([firstSentence.index(x) for x in firstSentence  if x in secondSentence])
print()

# Question 15
print("Question 15")
print([(x[0],y[0]) for x in firstSentence for y in secondSentence])
print()

# Part 2: Regular Expressions
import re
print("Part 2: Regular Expressions")
print()

text_file = open("lowerwords.txt", "r")
lines = text_file.readlines()
words = []
for line in lines:
   words.append(line.strip("\n"))


test = ['ababab','oops, oops','abba','nana my nana']
   
def filterList (regExp, strings):
    return([x for x in strings if re.search(regExp, x)])

def printList (regExp, strings):
    print([x for x in strings if re.search(regExp, x)])
    
#exp = r’e$’
print("Question 1")
printList(r'^(([a-z][a-z])\2).*\1$', test)


print("Question 2")
print(len(filterList(r'^[a-z]{3}d$', words)))
print()

print("Question 3")
print(len(filterList(r'^[aeiou]', words)))
print()

print("Question 4")
print(len(filterList(r'[aeiou]{2}$', words)))
print()

print("Question 5")
print(len(filterList(r'^([aeiou])[a-z]*\1$', words)))
print()

print("Question 6")
print(len(filterList(r'[aeiou]{4}', words)))
print()

print("Question 7")
print(len(filterList(r'(er)[a-z]*(er)[a-z]*(er)', words)))
print()

print("Question 8")
print(len(filterList(r'([a-z]{2})[a-z]*\1[a-z]*\1', words)))
print()

print("Question 9")
print(len(filterList(r'([a-z])([a-z])[a-z]*\2\1[a-z]*\1\2', words)))
print()

print("Question 10")
print(len(filterList(r'([a-z])\1[a-z]*([a-z])\2[a-z]*([a-z])\3', words)))
print()

print("Question 11")
print(len(filterList(r'([a-z])[a-z]\1[a-z]*([a-z])[a-z]\2', words)))
print()

print("Question 12")
print(len(filterList(r'([a-z])[a-z]\1([a-z])[a-z]\2([a-z])[a-z]\3', words)))



