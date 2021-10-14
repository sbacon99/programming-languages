#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:29:13 2021

@author: sam
"""
# import libraries
import itertools
import random
import time
from simple_colors import *


# create deck of cards (list of tuples)
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = list(itertools.product(values, suits))

# begin game
print("Ready to play War?")
inp = input("Press 'enter' to play: ")

while inp != '':
    print()
    print("Ready to play War?")
    inp = input("Press 'enter' to play: ")

# shuffling/splitting deck
random.shuffle(deck)                                                        
player_deck = deck[0:5]
computer_deck = deck[5:10]

print()
print("The deck has been shuffled")

# activite 'cheating' mode?
unlocked = input("Would you like to view the piles after each round? (Y or N) ")
if unlocked != "Y" and unlocked != "N":
    unlocked = input("Invalid response...Would you like to view the piles after each round? (Y or N): ")

# initialize round counter
round_counter = 1

# game loop
while not len(player_deck) == 0 and not len(computer_deck) == 0:
    play = input("Press 'enter' to play the next round: ")

    while play != '':
        print()
        play = input("Press 'enter' to play the next round: ")
        
    print()
    print("ROUND", round_counter)
    print()
    print("Your card is", player_deck[0],". The computer's card is", 
          computer_deck[0], ".")
    print()
    
    player_current = []
    computer_current = []
    
    player_current.insert(0,player_deck[0])
    computer_current.insert(0,computer_deck[0])
    player_deck.pop(0)
    computer_deck.pop(0)
  
# if player wins round...
# append both cards to player's deck
      
    if int(player_current[0][0]) > int(computer_current[0][0]):                     
        player_deck.append(player_current[0])                                       
        player_deck.append(computer_current[0])
        print(green("The cards have been added to your pile."))
        
# if computer wins round...
# append both cards to computer's deck

    elif int(player_current[0][0]) < int(computer_current[0][0]):                   
        computer_deck.append(computer_current[0])                                   
        computer_deck.append(player_current[0])
        print(red("The cards have ben added to the computer's pile"))  
        
# if there is a tie -- WAR!
# while the cards are equal...
    # append next card in deck to current
    # append next card in deck to current
    # 'pop' card off top of player_deck
    # 'pop' card off top of computer_deck
    
    else:                                                                           
        print("War!")
        print()
        while int(player_current[0][0]) == int(computer_current[0][0]):             
            player_current.insert(0,player_deck[0])                                     
            computer_current.insert(0,computer_deck[0])                                 
            player_deck.pop(0)                                                                                                    
            computer_deck.pop(0)                                                        
            output1 = ["Your next card is", "...", player_current[0]]                   
            for i in output1:                                                       
                time.sleep(1)                                                              
                print(i)     
                time.sleep(1)
            print()
            output2 = ["The computer's next card is", "...", computer_current[0]]   
            for i in output2:                                                       
                time.sleep(1)
                print(i)
                time.sleep(1)
  
# if player wins...
    # append all computer cards from round to player's deck
    # append all player cards from round to player's deck

            if int(player_current[0][0]) > int(computer_current[0][0]):             
                for card in computer_current:                                           
                    player_deck.append(card)
                for card in player_current:                                             
                    player_deck.append(card)
                print()
                print(green("The cards have been added to your pile."))
                
# if computer wins...               
    # append all computer cards from round to computer's deck
    # append all player cards from round to computer's deck
    
            if int(player_current[0][0]) < int(computer_current[0][0]):             
                for card in computer_current:                                           
                    computer_deck.append(card)
                for card in player_current:                                             
                    computer_deck.append(card)
                print()
                print(red("The cards have ben added to the computer's pile"))   

# if 'cheating mode' is on, print both decks after each round

    if unlocked == "Y":                                                             
        print()
        print("Your remaining deck:")
        print(player_deck)
        print()
        print("The computer's remaining deck:")
        print(computer_deck)
      
# print length of both piles after each round

    print()                                                                         
    print("You have", len(player_deck), "cards remaining.")
    print("The computer has", len(computer_deck), "cards remaining.")

    round_counter +=1     

# outcome
if len(player_deck) == 0:                                                           
    print()                                                                             
    print(red("You lose..."))
    
if len(computer_deck) == 0:                                                         
    print()                                                                             
    print(green("You win!"))


