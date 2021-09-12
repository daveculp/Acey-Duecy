import random
import time 

class Card:
	text_values = (None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King")
	suits = ("Clubs", "Diamonds", "Hearts", "Spades")
	
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
	def show(self):
		print ( '{0} of {1}'.format(Card.text_values[self.value], self.suit) )
		
	def get_value(self):
		return self.value
		
	def get_suit(self):
		return self.suit
		
	def __lt__(self, card):
		if self.value < card.value:
			return True
		if self.value == card.value:
			if Card.suits.index(self.suit) < Card.suits.index(card.suit):
				return True
		return False
		
	def __gt__(self, card):
		if self.value > card.value:
			return True
		if self.value == card.value:
			if Card.suits.index(self.suit) > Card.suits.index(card.suit):
				return True
		return False	
		
	def __eq__(self, card):
		if (self.value == card.value):
			return True
		else:
			return False
			
	def between(self, card1, card2):
		vals = [card1.value, card2.value]
		vals.sort()

		if (vals[0] == vals[1] == self.value):
			card1_suit = Card.suits.index(card1.suit)
			card2_suit = Card.suits.index(card2.suit)
			suits = [card1_suit, card2_suit]
			suits.sort()
			if suits[0] <  Card.suits.index(self.suit) < suits[1]:
				return True
			else:
				return False
			
		if vals[0] < self.value < vals[1]:
			return True
		else:
			return False
		
		
	def __str__(self):
		return '{0} of {1}'.format(Card.text_values[self.value], self.suit)

class Deck:
	def __init__(self):
		self.construct()

	def construct(self):
		self.cards = []
		for suit in Card.suits:
			for value in range(1,14):
				self.cards.append(Card(value,suit))
				
	def shuffle(self):
		random.shuffle(self.cards)
		
	def choose(self, remove = False):
		if len(self.cards) == 0:
			return None
		card = random.choice(self.cards)
		if remove:
			self.cards.remove(card)
		return card
		
	def get_next(self,remove = True):
		if len(self.cards) == 0:
			return None
		card = self.cards.pop(0)
		if remove==False:
			self.cards.append(card)
		return card
		
	def len(self):
		return len(self.cards)

	def show(self):
		for card in self.cards:
			card.show()

print ("Testing between")

card1 = Card(6,"Spades")
card2 = Card(6,"Diamonds")
card3 = Card(6,"Clubs")

print(card2.between(card3, card1) )
print ("""
This is the game of Acey-Duecy.  You start with a set amount of money.
Each turn you will be dealt two cards.  You will then place a bet,
betting whether the next card dealt will be between the first two cards.

In this game, the value of an Ace = 1

""")

deck = Deck()
deck.shuffle()
money = 200

while money > 0 and deck.len() >0:
	
	time.sleep(1)
	print("-----------------------------------------------------")
	print("You have ${0}".format(money) )
	
	card1 = deck.get_next()
	card2 = deck.get_next()
	
	print ("Card 1:", card1)
	print ("Card 2:", card2)
	
	bet = money+1
	while (bet > money) and (bet > 0):
		bet = input ("What is your bet? ")
		bet = int(bet)
	time.sleep(2)
	if bet == 0:
		print("Thats a chicken bet!")
		time.sleep(1)
		
	card3 = deck.get_next()
	print ("Card 3:", card3)
	time.sleep(1)
	if card3.between(card1,card2) and bet > 0:
		print ("YOU WIN!!!")
		money += bet
	elif bet > 0:
		print ("Sorry, you lose!")
		money -= bet
	time.sleep(1)
	
	time.sleep(1)
	print ("Cards left in the deck {0}".format( deck.len() ) )
	


	if deck.len() <=2:
		print("We have run though the deck!")
		break
		
print("\n"*4)
print("-----------------------------------------------------")		
print ("Game over!")
print ("You ended with ${0}".format(money))
		
		
	


