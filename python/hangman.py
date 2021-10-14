#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:21:29 2021

@author: sam
"""

import random

#dictionary = ['there','here','spend','mississippi','ball','relax','zipper','peer','pear','tame','team','zeep','zoop','pale']
#dictionary = ['ally','beta','cool','deal','else','flew','good','hope','ibex']
#dictionary = ['carrot']
        
# import dictionary.txt
text_file = open("dictionary.txt", "r")
lines = text_file.readlines()
dictionary = []
for line in lines:
   dictionary.append(line.strip("\n"))



# collect word length
print()
print("Ready to play Hangman?")
inp = input("Enter a word length: ")

while len(inp) == 0 or inp.isdigit() == False:
    inp = input("Please enter a valid length: ") 
   
while int(inp) <= 0 or int(inp) >= 30 or int(inp) == 26 or int(inp) == 27:
  inp = input("Please enter a valid length: ")
 
blank_word = "-"*int(inp)


  
# collect number of guesses
inp2 = input("Enter a guess total (between 1 and 25): ")

while len(inp2) == 0 or inp2.isdigit() == False:
    inp2 = input("Please enter a valid number: ") 
   
while int(inp2) <= 0 or int(inp2) > 25:
    inp2 = input("Number must be between 1 and 25: ")

guess_num = int(inp2)



# count of remaining words
inp3 = input("Would you like to view the running total of remaining words? (Y or N): ")
if inp3 != "Y" and inp3 != "N":
    inp3 = input("Invalid response...Would you like to view the running total of remaining words? (Y or N):")

# print all remaining words
inp4 = input("Would you like to view all remaining words? (Y or N): ")
if inp4 != "Y" and inp4 != "N":
    inp4 = input("Invalid response...Would you like to view all remaining words? (Y or N):")

# get dictionary words with correct length
curr_list = []
for word in dictionary:
    if len(word) == int(inp):
       curr_list.append(word)



# list of guessed letters
guessed_letters = []



# loop while the player still has guesses remaining and the word has not been solved
while guess_num > 0 and blank_word.find('-') != -1:
    
    # print remaining guesses, guessed letters, and progress
    print("Remaining guesses:", guess_num)
    print("Guessed letters:", guessed_letters)
    print("Current word:", blank_word)
    if inp3 == "Y" or inp3 == "y":
        print("Count of remaining words:", len(curr_list))
    if inp4 == "Y" or inp4 == "y":
        print("Possible words remaining:", curr_list)
  
    
  
    
# prompt player for guess 
    inp5 = input("Guess a letter: ")

    while not inp5.isalpha() or not len(inp5) == 1:
        inp5 = input("Try again. Guess a letter: ")

    while inp5.lower() in guessed_letters:
        inp5 = input("You have already guessed this letter. Guess another letter: ") 
        
    guess = inp5.lower()                                    # store guess
    guessed_letters.append(guess)                           # add guess to list of guesses
    
    # creating word families (dictionaries)
    index_dict = {}                                         # stores indices and counts
    word_dict = {}                                          # stores indices and words
        
    
    for word in curr_list:                                  # iterate through possible words
        indices = []                                        # initialize lists to store indices for word
        for i in range(0,len(word)):                        # iterate through characters in word
            if word[i] == guess:                            # if character == guess...
                indices.append(i)                               # add index to 'indices' list
        if len(indices) == 0:                               # if guess never appears in the word
            indices.append('none')                          # indices list will have 'none' 

        ind_str = ','.join(str(j) for j in indices)         # convert indices list to string (for dictionary)
        
        
        if ind_str in index_dict.keys():                            # if ind_str is already a key...
            index_dict[ind_str] += 1                                    # add one to the value (index_dict)
            word_dict[ind_str] = word_dict[ind_str] + ',' + word        # add word to value (word_dict)         
        else:                                                       # if ind_str is not a key...
            index_dict[ind_str] = 1                                     # set value = 1 (index_dict)
            word_dict[ind_str] =  word                                  # add word to value 
    
    sorted_families = sorted(index_dict, key=index_dict.get,    # sort index_dict by value
                             reverse=True)
    biggest_family = sorted_families[0]                         # get the family with the most words
            

    if biggest_family == 'none':                            # if the biggest family did not have the guess...
        guess_num -= 1                                          # subtract a guess from the player
    else:                                                   # otherwise...
        words = biggest_family.split(',')                       # split string of indices into a list
        for i in range(0, len(words)):
            words[i] = int(words[i])
        for i in words:
            blank_word = blank_word[:i] + guess + blank_word[i+1:]      # update output where necessary
            
    curr_list = word_dict[biggest_family].split(',')             # update current list 
    



# possible outcomes...

# win
if blank_word.find('-') == -1:
    print()
    print("Congratulations. You win!")
    print("The correct word was", blank_word)
# lose
else:      
    print()
    print("Sorry, you lose...")
    print("The correct word was", curr_list[random.randint(0, len(curr_list))])
 
        
  


    