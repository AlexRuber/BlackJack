#!/usr/bin/env python
# 
"""     
   BlackJack Game in Python - Alex Ruber

   Specs:
   1.) The game needs to have one player versus an automated dealer
   2.) The player needs to have one player versus an automated player
   3.) The player can stand or hit
   4.) The players must be able to pick their betting amount
   5.) You need to keep track of players total money
   6.) You need to alert the player of wins, losses, or busts
   7.) Must use OOP and Classes in some portion of the game

"""

import re
import os
import random


#Boolean used to know if hand is in play
playing = False

#Globals
chip_pool = 100 #raw input
bet = 1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

#Hearts, Diamonds, Clubs and Spades
suits = ('H', 'D', 'C', 'S')

#Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

#Point values dict
card_val = {'A':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}



class Player(object):

	def __init__(self, bankroll=100):
		self.bankroll = bankroll

	def adjust_bankroll(self, amount):
		self.bankroll += amount

	#Create the deck 
	def create_Deck(self):
		deck = [str(x)+y for x in range (1,14) for y in ["S", "H", "C", "D"]]
		print (deck)
	#Deals the Cards
	def deal_cards(self):
		pass

#Card Class
class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def grab_suit(self):
		return self.suit

	def grab_rank(self):
		return self.rank

	def draw(self):
		print (self.suit + self.rank)

#Hand Class
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		#Aces can be 1 or 11 so we need to define it here
		self.ace = False

		hand_comp = "" 

		for card in self.cards:
			card_name = card.__str__()
			hand_comp += " " + card_name

		return 'The hand has %s' %hand_comp

	def card_add(self,card):
		self.cards.append(card)

		#Check for Aces
		if card.rank == "A":
			self.ace = true
		self.value += card_val[card.rank]

	def calc_val(self):
		if(self.ace == True and self.value < 12):
			return self.value + 10
		else:
			return self.value

	def draw(self, hidden):
		if hidden == True and playing == True:
			#Don't show first hidden card
			starting_card = 1
		else:
			starting_card = 0
		for x in range(starting_card, len(self.cards)):
			self.cards[x].draw()


#Deck Class
class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit,rank))
	
	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

	def __str__(self):
		deck_comp = ""
		for card in self.cards:
			deck_comp += " " + deck.comp.__str__()

		return "The deck has" + deck_comp


































