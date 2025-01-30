import random
import time 

class Card: 
	#text_values = (None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen", "King", "Ace")
	card_values = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen", 13:"King", 14:"Ace"}
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
		return self.value == card.value
			
	def between(self, card1, card2):
		return min(card1, card2) < self < max(card1, card2)
		
	def show(self):
		print ( '{0} of {1}'.format(Card.card_values[self.value], Card.suits[self.suit]) )
		
	def __str__(self):
		return '{0} of {1}'.format(Card.card_values[self.value], Card.suits[self.suit])
		

class Deck:
	def __init__(self):
		random.seed()
		self.construct()

	def construct(self):
    		self.cards = [Card(value, suit) for suit in range(4) for value in range(2, 15)]
    		self.discards = []
				
	def shuffle(self):
		#first put any discards back into the deck and then empty the discards
		self.cards.extend(self.discards)
		self.discards = []
		random.shuffle(self.cards)

	def cut(self):
	    if len(self.cards) < 2:
	        return  # Not enough cards to cut
	
	    middle = len(self.cards) // 2
	    range_limit = min(8, middle)  # Ensures we don't go out of bounds
	    cut_point = random.randint(middle - range_limit, middle + range_limit)
	
	    # Perform the cut
	    self.cards = self.cards[cut_point:] + self.cards[:cut_point]
		
	def order(self):
		self.cards.sort()
		
	def choose_random(self, remove = True):
		if len(self.cards) == 0:
			return None
		card = random.choice(self.cards)
		if remove:
			self.cards.remove(card)
			self.discards.append(card)
		return card
		
	def get_next(self, remove=True, place="bottom"):
	    if not self.cards:
	        return None
	
	    card = self.cards.pop(0)  # Take the top card
	
	    if not remove:
	        if place == "top":
	            self.cards.insert(0, card)  # Put it back on top
	        elif place == "random":
	            self.cards.insert(random.randint(0, len(self.cards)), card)  # Insert randomly
	        else:  # Default: place at the bottom
	            self.cards.append(card)  
	
	    else:
	        self.discards.append(card)

    return card
		
	def __len__(self):
		return len(self.cards)
		
	def is_empty(self):
		if len(self.cards) == 0:
			return True
		else:
			return False

	def show(self):
		for card in self.cards:
			print(card)
