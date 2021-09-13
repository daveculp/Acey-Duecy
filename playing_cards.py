import random
import time 

class Card:
	text_values = (None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen", "King", "Ace")
	suits = ("Clubs", "Diamonds", "Hearts", "Spades")
	
	def __init__(self, value, suit):
		""" value (2-14) and suit(0-3) are ints """
		self.value = value
		self.suit = suit
	
	def get_suit_text(self):
		return Card.suits[self.suit]
		
	def __lt__(self, card):
		if self.value < card.value:
			return True
		if self.value == card.value:
			if self.suit < card.suit:
				return True
		return False
		
	def __gt__(self, card):
		if self.value > card.value:
			return True
		if self.value == card.value:
			if self.suit > card.suit:
				return True
		return False	
		
	def __eq__(self, card):
		if (self.value == card.value):
			return True
		return False
			
	def between(self, card1, card2):
		if (card1.value == card2.value) or (card1.value < card2.value):
			return card1 < self < card2
		else:
			return card2 < self < card1
	
	def __str__(self):
		return '{0} of {1}'.format(Card.text_values[self.value], Card.suits[self.suit])

class Deck:
	def __init__(self):
		random.seed()
		self.construct()

	def construct(self):
		self.cards = []
		self.discards = []
		for suit in range(len(Card.suits)):
			for value in range(2,15):
				self.cards.append(Card(value,suit))
				
	def shuffle(self):
		self.cards.extend(self.discards)
		random.shuffle(self.cards)
		
	def order(self):
		self.cards.sort()
		
	def choose_random(self, remove = False):
		if len(self.cards) == 0:
			return None
		card = random.choice(self.cards)
		if remove:
			self.cards.remove(card)
			self.discards.append(card)
		return card
		
	def get_next(self,remove = True):
		if len(self.cards) == 0:
			return None
		card = self.cards.pop(0)
		if remove==False:
			self.cards.append(card)
		else:
			self.discards.append(card)
		return card
		
	def __len__(self):
		return len(self.cards)

	def show(self):
		for card in self.cards:
			card.show()
