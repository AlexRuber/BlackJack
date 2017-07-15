#!/usr/bin/env python
# 
"""     
   Practice python with OOP 
"""

import sys
import os
import re
import random


#Greeting

name = raw_input('Welcome to Rock, Paper, Scissors! What is your name?: ')
print 'Hi %s' % (name)
userChoice =  raw_input('Please choose rock[r], paper[p], or scissors[s]: ')

#Generate Computers Choice 
choices = ['r', 'p', 's']
computerChoice = random.choice(choices)

#Rules Logic
#Draw
if userChoice == computerChoice:
	print "Draw game!"

#User wins
if userChoice == 'r' and computerChoice == 's':
	print "Rock vs Scissors"
	print "You win! :D"

if userChoice == 'p' and computerChoice == 'r':
	print "Paper vs Rock"
	print "You win! :D"

if userChoice == 's' and computerChoice == 'p':
	print 'Scissors vs Paper'
	print 'You win! :D'

#Computer wins
if computerChoice == 'r' and userChoice == 's':
	print 'Scissors vs Rock'
	print "You lose :("

if computerChoice == 'p' and userChoice == 'r':
	print 'Rocks vs Paper'
	print "You lose :("

if computerChoice == 's' and userChoice == 'p':
	print 'Paper vs Scissors'
	print 'You lose :('

